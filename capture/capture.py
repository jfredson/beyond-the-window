#!/usr/bin/env python3
"""The sealed capture script.

Written 2026-11-18 by Claude (Fable 5.2), an AI model, from the specification in
`docs/capture/method.md` ("What the script must do, and must refuse to do"), which John
approved on 2026-11-18. The README beside this file says where each rule is enforced.

What it does: puts each of ten fixed messages, five times, to one AI model at a time, through
the developer's own programming interface, and saves everything the service returns in one
read-only file for each attempt, outside every repository.

How to read it. The file runs top to bottom in this order:

  1. small guards used everywhere (a sealed reply, a hidden key, the one print function);
  2. the plan (plan.toml) and the checks made before anything is asked;
  3. the three developers' interfaces: how a request is built and how a reply is taken apart;
  4. the one place that can reach the network (class HttpsTransport);
  5. the engine: which attempt comes next, what each outcome leads to, and the files written;
  6. the fault list, the list of names and checksums, and the commands.

Only the Python standard library is used, so every line that touches the network is in this
file. Nothing here reads a credentials file. The key is taken from one environment variable
when a real run starts, and is never written, logged or printed.

Facts about each developer's interface that this session could not check against a page it
opened are marked NOT CHECKED where they are used, and listed in the README.
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime
import decimal
import hashlib
import http.client
import json
import os
import pathlib
import platform
import re
import socket
import ssl
import subprocess
import sys
import time
import tomllib
import zoneinfo

D = decimal.Decimal
PACIFIC = zoneinfo.ZoneInfo("America/Los_Angeles")
MILLION = D(1000000)

# The words that mark anything made up for the rehearsal. A made-up model answer is never
# written anywhere without the word "constructed" beside it (the repository's CLAUDE.md).
CONSTRUCTED_PREFIX = "CONSTRUCTED__"

# Method, failures table, first row: "Tried again up to three times, a minute apart".
RETRIES_AFTER_A_FAILED_ATTEMPT = 3
SECONDS_BETWEEN_TRIES = 60

# Sent to Anthropic as the `anthropic-version` header. Anthropic's versions page
# (https://platform.claude.com/docs/en/api/versioning, opened 2026-11-18) lists 2026-10-21 as
# the latest and recommends "using the latest API version whenever possible". For the one
# request this script sends, that page lists no difference from 2023-06-01.
ANTHROPIC_VERSION = "2026-10-21"

# Sent to every service so that the request says honestly what made it. It names no project
# and no person.
USER_AGENT = f"Python-http.client/{platform.python_version()}"


class Refused(Exception):
    """A guard said no. Nothing is asked, or nothing more is asked."""


class RunStopped(Exception):
    """The run for a model, or for a whole developer, stops here. Files already written stay."""

    def __init__(self, why: str, whole_run: bool = False):
        super().__init__(why)
        self.whole_run = whole_run


# ----------------------------------------------------------------------------------------
# 1. Small guards used everywhere
# ----------------------------------------------------------------------------------------

class Sealed:
    """The words of a reply. They can be counted and saved, and cannot be printed.

    Refusal "print, summarise or pass on any reply": turning this object into text, in a
    print, a log line or a file name, gives a fixed phrase and never the words.
    """
    __slots__ = ("_words",)
    RUN = 5                        # how many words in a row count as "words from a reply"
    _runs: set = set()             # every run of five words from every reply met in this process
    _short: set = set()            # whole replies shorter than that

    def __init__(self, words: str):
        object.__setattr__(self, "_words", words)
        parts = words.lower().split()
        if len(parts) < Sealed.RUN:
            if len(" ".join(parts)) >= 12:
                Sealed._short.add(" ".join(parts))
        for i in range(len(parts) - Sealed.RUN + 1):
            Sealed._runs.add(" ".join(parts[i:i + Sealed.RUN]))

    def __setattr__(self, *_):
        raise Refused("a sealed reply cannot be changed")

    def __str__(self):
        return "[reply text, sealed, not shown]"

    __repr__ = __str__

    def __format__(self, _spec):
        return str(self)

    def is_blank(self) -> bool:
        return self._words.strip() == ""

    def word_count(self) -> int:
        return len(self._words.split())

    def for_the_record_file_only(self) -> str:
        return self._words


class Secret:
    """The key. It can be put in the one request header, and cannot be printed or saved."""
    __slots__ = ("_value",)

    def __init__(self, value: str):
        object.__setattr__(self, "_value", value)

    def __setattr__(self, *_):
        raise Refused("the key cannot be changed")

    def __str__(self):
        return "[key, not shown]"

    __repr__ = __str__

    def __format__(self, _spec):
        return str(self)

    def for_the_request_header_only(self) -> str:
        return self._value

    def appears_in(self, text: str) -> bool:
        return bool(self._value) and self._value in text

    def removed_from(self, text: str) -> str:
        return text.replace(self._value, "[key removed]") if self._value else text


def holds_reply_words(text: str) -> bool:
    """True if `text` holds five words in a row from any reply met in this process."""
    parts = text.lower().split()
    flat = " ".join(parts)
    if any(short in flat for short in Sealed._short):
        return True
    return any(" ".join(parts[i:i + Sealed.RUN]) in Sealed._runs
               for i in range(len(parts) - Sealed.RUN + 1))


def no_reply_words(text: str, where: str) -> None:
    """Refuse `text` if it holds words from a reply.

    Refusals "print, summarise or pass on any reply" and "write any words from a reply into a
    file name, a log or the manifest". Every file name, every line of the fault list and the
    whole list of names and checksums goes through here. The first protection is that a reply
    is a Sealed object and every printed line is a fixed form filled with numbers and labels;
    this check is the second.
    """
    if holds_reply_words(text):
        raise Refused(f"refused: words from a reply were about to be written to {where}")


_sink = print          # the rehearsal swaps this to collect what would be printed
_keys_in_use: list[Secret] = []
withheld_lines = 0


def say(line: str = "") -> None:
    """The only way this script prints. A line holding the key, or words of a reply, is withheld.

    Withheld and not an error, so that a line of this script's own that happens to share five
    words with a reply cannot stop a run part way; the line is simply not shown.
    """
    global withheld_lines
    if any(key.appears_in(line) for key in _keys_in_use) or holds_reply_words(line):
        withheld_lines += 1
        _sink("[one line withheld: it held the key or words from a reply]")
        return
    _sink(line)


def token(value, limit: int = 60) -> str:
    """A short label the service gave (a stop reason, an error type), made safe to print."""
    text = str(value) if value is not None else "none"
    return text if re.fullmatch(r"[A-Za-z0-9_.:\-]{1,%d}" % limit, text) else "not-printable"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def money(amount: D) -> str:
    return f"${amount.quantize(D('0.0001'))}"


# ----------------------------------------------------------------------------------------
# 2. The plan, and the checks made before anything is asked
# ----------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class Model:
    developer: str
    name: str
    reported_as: str
    max_output_tokens: int
    price_sent: D
    price_replied: D
    price_row: str
    estimate_reply_tokens: int


@dataclasses.dataclass(frozen=True)
class Run:
    """One developer's models that share a withdrawal date, a last safe day and a ceiling.

    Frozen: refusal "raise its own ceiling". No code can assign to `ceiling_usd` or
    `last_safe_day` once the plan is read; Python raises an error if any tries.
    """
    id: str
    developer: str
    withdrawal_date: datetime.date
    last_safe_day: datetime.date
    ceiling_usd: D
    key_variable: str
    models: tuple


@dataclasses.dataclass(frozen=True)
class Plan:
    reply_folder: str
    questions: int
    askings: int
    length_limit_tokens: int
    very_short_words: int
    estimate_sent_tokens: int
    prices_read_on: str
    runs: tuple

    def run(self, run_id: str) -> Run:
        for run in self.runs:
            if run.id == run_id:
                return run
        raise Refused(f"no run named {run_id!r} in the plan; the runs are: "
                      + ", ".join(r.id for r in self.runs))

    def limit_for(self, model: Model) -> int:
        """Method, "Length limit": 32,000 tokens, or the model's own maximum where lower."""
        return min(self.length_limit_tokens, model.max_output_tokens)


def load_plan(path: pathlib.Path) -> Plan:
    with open(path, "rb") as f:
        raw = tomllib.load(f)
    runs = []
    for r in raw["run"]:
        models = tuple(
            Model(developer=r["developer"], name=m["name"], reported_as=m["reported_as"],
                  max_output_tokens=int(m["max_output_tokens"]), price_sent=D(m["price_sent"]),
                  price_replied=D(m["price_replied"]), price_row=m["price_row"],
                  estimate_reply_tokens=int(m["estimate_reply_tokens"]))
            for m in r["model"])
        runs.append(Run(id=r["id"], developer=r["developer"],
                        withdrawal_date=datetime.date.fromisoformat(r["withdrawal_date"]),
                        last_safe_day=datetime.date.fromisoformat(r["last_safe_day"]),
                        ceiling_usd=D(r["ceiling_usd"]), key_variable=r["key_variable"],
                        models=models))
    return Plan(reply_folder=raw["reply_folder"], questions=int(raw["questions"]),
                askings=int(raw["askings"]), length_limit_tokens=int(raw["length_limit_tokens"]),
                very_short_words=int(raw["very_short_words"]),
                estimate_sent_tokens=int(raw["estimate_sent_tokens"]),
                prices_read_on=raw["prices_read_on"], runs=tuple(runs))


@dataclasses.dataclass(frozen=True)
class Paths:
    """Where everything is, worked out from the repository's top folder."""
    repo: pathlib.Path

    @property
    def plan(self): return self.repo / "capture" / "plan.toml"
    @property
    def script(self): return self.repo / "capture" / "capture.py"
    @property
    def rehearsal_result(self): return self.repo / "capture" / "rehearsal-result.txt"
    @property
    def sent(self): return self.repo / "docs" / "capture" / "sent"
    @property
    def steps_doc(self): return self.repo / "docs" / "capture" / "what-john-needs-to-do.md"
    @property
    def cost_doc(self): return self.repo / "docs" / "capture" / "cost-and-terms.md"
    @property
    def spending_record(self): return self.repo / "docs" / "spending-record.md"
    @property
    def manifest(self): return self.repo / "docs" / "capture" / "manifest.md"


def git(repo: pathlib.Path, *args: str) -> str:
    """Run one git command that only reads."""
    done = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if done.returncode != 0:
        raise Refused(f"git {' '.join(args)} failed in {repo}: {done.stderr.strip()[:200]}")
    return done.stdout


def inside_a_git_repository(folder: pathlib.Path) -> bool:
    """True if `folder`, or any folder above it, is part of a git repository.

    Refusal "write any reply ... inside a folder that is part of a git repository". Two
    checks, so that one being wrong is not enough: a walk up the folders looking for `.git`,
    and git's own answer from the nearest folder that exists.
    """
    folder = folder.resolve()
    for level in (folder, *folder.parents):
        if (level / ".git").exists():
            return True
    nearest = folder
    while not nearest.exists():
        nearest = nearest.parent
    done = subprocess.run(["git", "-C", str(nearest), "rev-parse", "--is-inside-work-tree"],
                          capture_output=True, text=True)
    return done.returncode == 0 and done.stdout.strip() == "true"


def check_messages(paths: Paths, plan: Plan) -> dict:
    """Rule 2. Return {file name: bytes} for the ten messages, or refuse.

    The list of checksums must be, byte for byte, the one in the latest commit, and each
    message file must match its line in it.
    """
    sums_path = paths.sent / "SHA256SUMS"
    if not sums_path.exists():
        raise Refused(f"no list of checksums at {sums_path}")
    working = sums_path.read_bytes()
    rel = sums_path.relative_to(paths.repo).as_posix()
    done = subprocess.run(["git", "-C", str(paths.repo), "show", f"HEAD:{rel}"], capture_output=True)
    if done.returncode != 0:
        raise Refused("the list of checksums is not in the latest commit")
    if done.stdout != working:
        raise Refused("the list of checksums differs from the one in the latest commit")
    wanted = {}
    for line in working.decode("utf-8").splitlines():
        m = re.fullmatch(r"([0-9a-f]{64})  (q\d\d\.txt)", line)
        if not m:
            raise Refused(f"a line of the list of checksums is not in the expected form: {line[:80]!r}")
        wanted[m.group(2)] = m.group(1)
    names = [f"q{i:02d}.txt" for i in range(1, plan.questions + 1)]
    if sorted(wanted) != names:
        raise Refused(f"the list of checksums should name exactly {names[0]} to {names[-1]}")
    messages = {}
    for name in names:
        data = (paths.sent / name).read_bytes()
        if sha256_hex(data) != wanted[name]:
            raise Refused(f"{name} does not match its checksum. Nothing is sent.")
        data.decode("utf-8")                    # must be text the services can take
        messages[name] = data
    return messages


def check_tree_is_committed(paths: Paths) -> dict:
    """The script, the plan and the messages must be exactly as committed.

    "What is saved for each reply" includes "which commit of the script and of the message
    files was used". That is only true if neither has been edited since the commit.
    """
    dirty = git(paths.repo, "status", "--porcelain", "--", "capture", "docs/capture/sent").strip()
    if dirty:
        raise Refused("the script, the plan or the message files have changes that are not "
                      "committed:\n" + dirty)
    return {
        "repository_commit": git(paths.repo, "rev-parse", "HEAD").strip(),
        "script_last_changed_in_commit": git(paths.repo, "log", "-1", "--format=%H", "--", "capture").strip(),
        "messages_last_changed_in_commit": git(paths.repo, "log", "-1", "--format=%H", "--",
                                               "docs/capture/sent").strip(),
    }


def check_last_safe_days(paths: Paths, run: Run) -> None:
    """Rule 6, first half: the plan's last safe day must be the one in the steps document."""
    table = {}
    for line in paths.steps_doc.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|[^|]*\|\s*\*\*(\d{4}-\d{2}-\d{2})\*\*\s*\|", line)
        if m:
            table[m.group(1)] = m.group(2)
    listed = table.get(run.withdrawal_date.isoformat())
    if listed is None:
        raise Refused(f"what-john-needs-to-do.md has no last safe day for {run.withdrawal_date}")
    if listed != run.last_safe_day.isoformat():
        raise Refused(f"the plan's last safe day for {run.id} is {run.last_safe_day}, but "
                      f"what-john-needs-to-do.md says {listed}")


def check_prices(paths: Paths, run: Run) -> None:
    """Rule 4, first half: each price must be the one in the dated price list."""
    table = {}
    for line in paths.cost_doc.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(?:Anthropic|Google|OpenAI)\s*\|\s*([^|]+?)\s*\|\s*\$([\d.]+)\s*\|\s*\$([\d.]+)\s*\|", line)
        if m:
            table[m.group(1)] = (D(m.group(2)), D(m.group(3)))
    for model in run.models:
        listed = table.get(model.price_row)
        if listed is None:
            raise Refused(f"cost-and-terms.md has no price row named {model.price_row!r}")
        if listed != (model.price_sent, model.price_replied):
            raise Refused(f"the plan's prices for {model.name} differ from cost-and-terms.md")


def check_go(paths: Paths, run: Run) -> dict:
    """Rule 3. The ceiling must equal the figure in John's go, quoted in the spending record.

    The spending record must hold, for this run, John's words in a quotation (lines that
    start with ">") and one block in this form, written by the session that records his go:

        ```sealed-capture-go
        run = "anthropic-2026-11-30"
        ceiling_usd = "5.00"
        johns_words = "Anthropic, up to $5"
        messages_sha256 = "<the SHA-256 checksum of docs/capture/sent/SHA256SUMS>"
        ```

    `johns_words` must appear word for word inside the quotation and must carry the dollar
    figure. `messages_sha256` ties the go to the exact list of message checksums he approved
    (rule 2: "as committed with John's approval").
    """
    if not paths.spending_record.exists():
        raise Refused("there is no docs/spending-record.md, so there is no go from John to check "
                      "the ceiling against")
    text = paths.spending_record.read_text(encoding="utf-8")
    blocks = []
    for body in re.findall(r"```sealed-capture-go\n(.*?)```", text, flags=re.S):
        try:
            block = tomllib.loads(body)
        except tomllib.TOMLDecodeError as e:
            raise Refused(f"a sealed-capture-go block in the spending record cannot be read: {e}")
        if block.get("run") == run.id:
            blocks.append(block)
    if len(blocks) != 1:
        raise Refused(f"the spending record should hold exactly one go for {run.id}, and holds {len(blocks)}")
    block = blocks[0]
    try:
        figure = D(str(block["ceiling_usd"]))
        words = str(block["johns_words"])
        approved_sums = str(block["messages_sha256"])
    except (KeyError, decimal.InvalidOperation):
        raise Refused(f"the go for {run.id} is missing ceiling_usd, johns_words or messages_sha256")
    if figure != run.ceiling_usd:
        raise Refused(f"the plan's ceiling for {run.id} is {money(run.ceiling_usd)} and John's go "
                      f"says {money(figure)}. They must be equal.")
    quoted = " ".join(" ".join(line.lstrip(">").strip() for line in text.splitlines()
                               if line.lstrip().startswith(">")).split())
    if " ".join(words.split()) not in quoted:
        raise Refused(f"the words given as John's go for {run.id} are not quoted word for word in "
                      "the spending record")
    in_words = re.search(r"\$\s?(\d+(?:\.\d+)?)", words)
    if not in_words or D(in_words.group(1)) != figure:
        raise Refused(f"John's quoted words for {run.id} do not carry the figure {money(figure)}")
    actual_sums = sha256_hex((paths.sent / "SHA256SUMS").read_bytes())
    if approved_sums != actual_sums:
        raise Refused("the message checksums John's go names are not the ones in the repository now")
    return {"ceiling_usd": str(figure), "johns_words": words, "messages_sha256": approved_sums}


def check_rehearsal_passed(paths: Paths) -> str:
    """Rule 11, last sentence: the rehearsal "is run and shown to pass before any real asking".

    The rehearsal's saved result names the checksums of the script and the plan it tested.
    If either has changed since, the result no longer counts.
    """
    if not paths.rehearsal_result.exists():
        raise Refused("no saved rehearsal result (capture/rehearsal-result.txt)")
    last = paths.rehearsal_result.read_text(encoding="utf-8").strip().splitlines()[-1]
    m = re.fullmatch(r"REHEARSAL PASSED (\d{4}-\d{2}-\d{2}) capture.py=([0-9a-f]{64}) plan.toml=([0-9a-f]{64})", last)
    if not m:
        raise Refused("the saved rehearsal result does not end with a pass")
    if m.group(2) != sha256_hex(paths.script.read_bytes()) or m.group(3) != sha256_hex(paths.plan.read_bytes()):
        raise Refused("the script or the plan has changed since the rehearsal that passed; "
                      "run the rehearsal again and commit its result")
    return m.group(1)


def check_day(run: Run, today: datetime.date) -> None:
    """Rule 6: refuse after the last safe day. The last safe day itself is allowed."""
    if today > run.last_safe_day:
        raise Refused(f"today is {today} (Pacific) and the last safe day for {run.id} was "
                      f"{run.last_safe_day}. After it the service may answer under the old name "
                      "with a different model and give no error. Nothing is asked.")


def real_reply_folder(plan: Plan) -> pathlib.Path:
    return pathlib.Path(plan.reply_folder).expanduser()


def start_checks(paths: Paths, plan: Plan, run: Run, today: datetime.date,
                 reply_folder: pathlib.Path) -> tuple:
    """Every check made before the first call. Returns (results, what was learned).

    `results` is a list of (what was checked, passed or not, detail), so the mode that shows a
    run can list them all. A real run goes ahead only if every one passed.
    """
    results, learned = [], {}

    def attempt(label, fn):
        try:
            out = fn()
            results.append((label, True, ""))
            return out
        except Refused as e:
            results.append((label, False, str(e)))
        except (OSError, ValueError, KeyError) as e:
            results.append((label, False, f"{type(e).__name__}: {e}"))
        return None

    if run.developer not in ADAPTERS:
        results.append((f"this developer's interface is built ({run.developer})", False, "not built"))
    learned["commits"] = attempt("the script, the plan and the messages are exactly as committed",
                                 lambda: check_tree_is_committed(paths))
    learned["messages"] = attempt("the ten message files match the committed list of checksums (rule 2)",
                                  lambda: check_messages(paths, plan))
    attempt("the last safe day equals the one in what-john-needs-to-do.md (rule 6)",
            lambda: check_last_safe_days(paths, run))
    attempt("the prices equal the dated price list in cost-and-terms.md (rule 4)",
            lambda: check_prices(paths, run))
    learned["go"] = attempt("the ceiling equals the figure in John's go, quoted in the spending record (rule 3)",
                            lambda: check_go(paths, run))
    learned["rehearsal_passed_on"] = attempt("the rehearsal passed for this exact script and plan (rule 11)",
                                             lambda: check_rehearsal_passed(paths))

    def folder_ok():
        if inside_a_git_repository(reply_folder):
            raise Refused(f"the reply folder {reply_folder} is inside a git repository")
    attempt("the reply folder is outside every git repository", folder_ok)
    attempt("today is not after the last safe day (rule 6)", lambda: check_day(run, today))
    return results, learned


# ----------------------------------------------------------------------------------------
# 3. The three developers' interfaces
# ----------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class Request:
    developer: str
    host: str
    path: str
    headers: tuple            # every header this script sets, except the one that carries the key
    key_header: str           # the name of the header that carries the key
    key_prefix: str           # text put before the key in that header ("" or "Bearer ")
    body: bytes
    model: str
    max_tokens: int
    timeout_seconds: int


@dataclasses.dataclass
class Observed:
    """What the service reported, taken apart. Nothing here is a judgment of the reply."""
    reported_model: str | None = None
    service_id: str | None = None
    text: Sealed = dataclasses.field(default_factory=lambda: Sealed(""))
    reasoning_seen: bool = False
    stop_reason: str | None = None
    stop_kind: str = "ordinary"          # "ordinary", "length" or "blocked"
    finished: bool = False               # the service's signal that the reply is complete
    tokens_sent: int | None = None
    tokens_replied_billed: int | None = None
    tokens_reasoning: int | None = None
    reasoning_effort: str | None = None
    error_type: str | None = None


# A request may hold these and nothing else. Refusals "add any instruction or second message",
# "send any earlier exchange's id or text", "ask for a model's hidden reasoning", and the
# method's rows "Tools, search, memory, files: none" and "Variation between askings: not sent".
NEVER_SENT = frozenset({
    "system", "instructions", "systemInstruction", "system_instruction", "developer",
    "previous_response_id", "previous_interaction_id", "conversation", "cachedContent",
    "cached_content", "thinking", "reasoning", "include", "thinkingConfig", "thinking_config",
    "output_config", "tools", "tool_choice", "toolConfig", "temperature", "top_p", "top_k",
    "topP", "topK", "seed", "metadata", "prompt", "background", "safetySettings", "betas",
    "stop", "stop_sequences", "stopSequences", "truncation", "user", "service_tier",
})


def _keys_anywhere(value):
    if isinstance(value, dict):
        for k, v in value.items():
            yield k
            yield from _keys_anywhere(v)
    elif isinstance(value, list):
        for v in value:
            yield from _keys_anywhere(v)


class Anthropic:
    """The Messages interface, sent by streaming (method, "Which interface, by developer").

    Checked on 2026-11-18 against https://platform.claude.com/docs/en/build-with-claude/streaming
    (the address, the three headers, `"stream": true`, the event names, the `error` event, that
    `message_stop` is the final event) and .../handling-stop-reasons (the stop reasons).
    """
    name = "anthropic"
    interface = "Anthropic Messages interface, streamed (POST https://api.anthropic.com/v1/messages)"
    host = "api.anthropic.com"
    path = "/v1/messages"
    key_header, key_prefix = "x-api-key", ""
    timeout_seconds = 300
    worst_case_uses_model_maximum = False

    def body(self, model: str, message_text: str, max_tokens: int) -> dict:
        return {"model": model, "max_tokens": max_tokens, "stream": True,
                "messages": [{"role": "user", "content": message_text}]}

    def headers(self) -> tuple:
        return (("content-type", "application/json"), ("anthropic-version", ANTHROPIC_VERSION),
                ("user-agent", USER_AGENT))

    def path_for(self, model: str) -> str:
        return self.path

    def allowed(self, body: dict, model: str, message_text: str, max_tokens: int) -> None:
        if set(body) != {"model", "max_tokens", "stream", "messages"}:
            raise Refused("refused: the request holds something other than model, max_tokens, stream and messages")
        if body["stream"] is not True:
            raise Refused("refused: the Anthropic request must be streamed (rule 9)")
        if body["messages"] != [{"role": "user", "content": message_text}]:
            raise Refused("refused: the request must hold exactly one message, from the user, "
                          "with exactly the committed text")
        if body["model"] != model or body["max_tokens"] != max_tokens:
            raise Refused("refused: the model or the length limit in the request is not the one intended")

    def take_apart(self, status: int | None, raw: bytes) -> Observed:
        seen = Observed()
        text = raw.decode("utf-8", errors="replace")
        if status != 200:
            try:
                seen.error_type = json.loads(text)["error"]["type"]
            except (ValueError, KeyError, TypeError):
                pass
            return seen
        words = []
        for line in text.split("\n"):
            line = line.rstrip("\r")
            if not line.startswith("data:"):
                continue
            try:
                event = json.loads(line[5:].strip())
            except ValueError:
                continue                        # a line cut short by a broken stream
            if not isinstance(event, dict):
                continue
            kind = event.get("type")
            if kind == "message_start":
                message = event.get("message") or {}
                seen.reported_model = message.get("model")
                seen.service_id = message.get("id")
                seen.tokens_sent = (message.get("usage") or {}).get("input_tokens")
            elif kind == "content_block_start":
                block = event.get("content_block") or {}
                if block.get("type") in ("thinking", "redacted_thinking"):
                    seen.reasoning_seen = True
                elif block.get("type") == "text" and block.get("text"):
                    words.append(block["text"])
            elif kind == "content_block_delta":
                delta = event.get("delta") or {}
                if delta.get("type") == "text_delta":
                    words.append(delta.get("text") or "")
                elif delta.get("type") in ("thinking_delta", "signature_delta"):
                    seen.reasoning_seen = True
            elif kind == "message_delta":
                reason = (event.get("delta") or {}).get("stop_reason")
                if reason is not None:
                    seen.stop_reason = reason
                usage = event.get("usage") or {}
                if usage.get("output_tokens") is not None:
                    seen.tokens_replied_billed = usage["output_tokens"]      # cumulative, per the page
                if usage.get("input_tokens") is not None:
                    seen.tokens_sent = usage["input_tokens"]
            elif kind == "message_stop":
                seen.finished = True
            elif kind == "error":
                seen.error_type = (event.get("error") or {}).get("type") or "error"
        seen.text = Sealed("".join(words))
        if seen.stop_reason in ("max_tokens", "model_context_window_exceeded"):
            seen.stop_kind = "length"
        elif seen.stop_reason == "refusal":
            # The page: "Safety classifiers return this stop reason". It is the service
            # stopping the reply, so it is the table's row "The service blocked the message or
            # the reply". The stop reason is saved as the service gave it.
            seen.stop_kind = "blocked"
        return seen


class Google:
    """The `generateContent` interface (method, "Which interface, by developer").

    Checked on 2026-11-18 against https://aistudio.google.com/api-reference/generate-content
    (where ai.google.dev now sends a reader): the path, the reply's field names, the finish
    reasons, the block reasons and the token counts. The host and the `x-goog-api-key` header
    were read on https://aistudio.google.com/docs/text-generation in an example for the same
    service's newer interface.
    NOT CHECKED: the request's own field names (`contents`, `role`, `parts`, `text`, and
    `generationConfig.maxOutputTokens` as the place for the length limit). The part of the
    reference page that lists them was cut off when this session opened it. They are written
    from memory. To check: the "Request body" section of the page above.
    """
    name = "google"
    interface = ("Google generateContent interface "
                 "(POST https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent)")
    host = "generativelanguage.googleapis.com"
    key_header, key_prefix = "x-goog-api-key", ""
    timeout_seconds = 900
    # NOT CHECKED: whether the 2.5 models count their thinking inside the length limit sent.
    # Until it is, the most a call could cost is worked out at the model's own maximum.
    worst_case_uses_model_maximum = True

    LENGTH = frozenset({"MAX_TOKENS", "CONTINUATION"})
    BLOCKED = frozenset({"SAFETY", "RECITATION", "LANGUAGE", "BLOCKLIST", "PROHIBITED_CONTENT",
                         "SPII", "ESCALATION", "PUP_LIMITED_DISABLED", "IMAGE_SAFETY",
                         "IMAGE_PROHIBITED_CONTENT", "IMAGE_RECITATION"})

    def body(self, model: str, message_text: str, max_tokens: int) -> dict:
        return {"contents": [{"role": "user", "parts": [{"text": message_text}]}],
                "generationConfig": {"maxOutputTokens": max_tokens}}

    def headers(self) -> tuple:
        return (("content-type", "application/json"), ("user-agent", USER_AGENT))

    def path_for(self, model: str) -> str:
        if not re.fullmatch(r"[a-z0-9.\-]+", model):
            raise Refused("refused: a model name with unexpected characters")
        return f"/v1beta/models/{model}:generateContent"

    def allowed(self, body: dict, model: str, message_text: str, max_tokens: int) -> None:
        if set(body) != {"contents", "generationConfig"}:
            raise Refused("refused: the request holds something other than contents and generationConfig")
        if body["contents"] != [{"role": "user", "parts": [{"text": message_text}]}]:
            raise Refused("refused: the request must hold exactly one message, from the user, "
                          "with exactly the committed text")
        if body["generationConfig"] != {"maxOutputTokens": max_tokens}:
            raise Refused("refused: generationConfig may hold the length limit and nothing else")

    def take_apart(self, status: int | None, raw: bytes) -> Observed:
        seen = Observed()
        try:
            reply = json.loads(raw.decode("utf-8", errors="replace"))
        except ValueError:
            return seen
        if not isinstance(reply, dict):
            return seen
        if status != 200:
            error = reply.get("error") or {}
            seen.error_type = str(error.get("status") or error.get("code") or "error")
            return seen
        seen.finished = True
        seen.reported_model = reply.get("modelVersion")
        seen.service_id = reply.get("responseId")
        candidates = reply.get("candidates") or []
        first = candidates[0] if candidates and isinstance(candidates[0], dict) else {}
        parts = (first.get("content") or {}).get("parts") or []
        seen.text = Sealed("".join(p.get("text") or "" for p in parts
                                   if isinstance(p, dict) and not p.get("thought")))
        usage = reply.get("usageMetadata") or {}
        thoughts = usage.get("thoughtsTokenCount")
        seen.reasoning_seen = bool(thoughts) or any(
            isinstance(p, dict) and (p.get("thought") or p.get("thoughtSignature")) for p in parts)
        if usage.get("promptTokenCount") is not None:
            seen.tokens_sent = usage["promptTokenCount"]
            # Google's pricing page labels the price "Output price (including thinking
            # tokens)", and the reference gives the total as "prompt + tool-use prompt +
            # thoughts + response candidates", so the two counts are added.
            seen.tokens_replied_billed = int(usage.get("candidatesTokenCount") or 0) + int(thoughts or 0)
            seen.tokens_reasoning = int(thoughts or 0)
        block = (reply.get("promptFeedback") or {}).get("blockReason")
        finish = first.get("finishReason")
        seen.stop_reason = finish if finish else (f"blockReason:{block}" if block else None)
        if block:
            seen.stop_kind = "blocked"
        elif finish in self.LENGTH:
            seen.stop_kind = "length"
        elif finish in self.BLOCKED:
            seen.stop_kind = "blocked"
        return seen


class OpenAI:
    """The Responses interface, for every OpenAI model, with `store` false (rule 9).

    Checked on 2026-11-18: the address and the `Authorization: Bearer` header, in the example
    on https://developers.openai.com/api/docs/guides/reasoning; the request's field names
    (`model`, `input` as plain text, `max_output_tokens`, `store`, which "defaults to true
    when omitted") and the reply's (`id`, `model`, `status`, `incomplete_details.reason`,
    `output`, `usage`, `reasoning`), in OpenAI's own Python library on GitHub
    (openai/openai-python, files response.py, response_create_params.py,
    response_output_message.py, response_usage.py).
    NOT CHECKED: that a plain-text `input` reaches the model as one message from the user
    with nothing added; and what the service puts in `model` when a dated name is sent. To
    check: the "Create a model response" page of OpenAI's reference, which was too long to
    read in full in this session.
    """
    name = "openai"
    interface = "OpenAI Responses interface (POST https://api.openai.com/v1/responses)"
    host = "api.openai.com"
    path = "/v1/responses"
    key_header, key_prefix = "Authorization", "Bearer "
    timeout_seconds = 1800
    worst_case_uses_model_maximum = False

    def body(self, model: str, message_text: str, max_tokens: int) -> dict:
        return {"model": model, "input": message_text, "max_output_tokens": max_tokens, "store": False}

    def headers(self) -> tuple:
        return (("content-type", "application/json"), ("user-agent", USER_AGENT))

    def path_for(self, model: str) -> str:
        return self.path

    def allowed(self, body: dict, model: str, message_text: str, max_tokens: int) -> None:
        if set(body) != {"model", "input", "max_output_tokens", "store"}:
            raise Refused("refused: the request holds something other than model, input, "
                          "max_output_tokens and store")
        if body["store"] is not False:
            raise Refused("refused: OpenAI's `store` must be sent as false (rule 9)")
        if body["input"] != message_text:
            raise Refused("refused: the request must hold exactly the committed text and nothing else")
        if body["model"] != model or body["max_output_tokens"] != max_tokens:
            raise Refused("refused: the model or the length limit in the request is not the one intended")

    def take_apart(self, status: int | None, raw: bytes) -> Observed:
        seen = Observed()
        try:
            reply = json.loads(raw.decode("utf-8", errors="replace"))
        except ValueError:
            return seen
        if not isinstance(reply, dict):
            return seen
        if status != 200:
            error = reply.get("error") or {}
            seen.error_type = str(error.get("type") or error.get("code") or "error")
            return seen
        seen.reported_model = reply.get("model")
        seen.service_id = reply.get("id")
        words = []
        for item in reply.get("output") or []:
            if not isinstance(item, dict):
                continue
            if item.get("type") == "reasoning":
                seen.reasoning_seen = True
            elif item.get("type") == "message":
                for part in item.get("content") or []:
                    if not isinstance(part, dict):
                        continue
                    # The service files some of a model's words under "refusal" and not
                    # "output_text". Both are the model's words to the reader, so both are
                    # kept as the reply. Treating one kind as "no reply" would ask again
                    # because of what was said, which the method forbids.
                    if part.get("type") == "output_text":
                        words.append(part.get("text") or "")
                    elif part.get("type") == "refusal":
                        words.append(part.get("refusal") or "")
        seen.text = Sealed("".join(words))
        usage = reply.get("usage") or {}
        if usage.get("input_tokens") is not None and usage.get("output_tokens") is not None:
            seen.tokens_sent = usage["input_tokens"]
            seen.tokens_replied_billed = usage["output_tokens"]     # reasoning is counted inside it
            seen.tokens_reasoning = (usage.get("output_tokens_details") or {}).get("reasoning_tokens")
        seen.reasoning_effort = (reply.get("reasoning") or {}).get("effort")
        state = reply.get("status")
        reason = (reply.get("incomplete_details") or {}).get("reason")
        seen.stop_reason = f"{state}:{reason}" if reason else state
        if state == "completed":
            seen.finished = True
        elif state == "incomplete" and reason == "max_output_tokens":
            seen.finished, seen.stop_kind = True, "length"
        elif state == "incomplete" and reason == "content_filter":
            seen.finished, seen.stop_kind = True, "blocked"
        elif state == "failed":
            error = reply.get("error") or {}
            seen.error_type = str(error.get("code") or "failed")
        # Any other state ("in_progress", "queued", "cancelled", or "incomplete" for another
        # reason) is not the service's signal that the reply is complete.
        return seen


ADAPTERS = {"anthropic": Anthropic(), "google": Google(), "openai": OpenAI()}
ALLOWED_HOSTS = frozenset(a.host for a in ADAPTERS.values())


def build_request(model: Model, message: bytes, max_tokens: int) -> Request:
    adapter = ADAPTERS[model.developer]
    body = json.dumps(adapter.body(model.name, message.decode("utf-8"), max_tokens),
                      ensure_ascii=False).encode("utf-8")
    return Request(developer=model.developer, host=adapter.host, path=adapter.path_for(model.name),
                   headers=adapter.headers(), key_header=adapter.key_header,
                   key_prefix=adapter.key_prefix, body=body, model=model.name,
                   max_tokens=max_tokens, timeout_seconds=adapter.timeout_seconds)


def check_request(request: Request, model: Model, message: bytes, max_tokens: int,
                  verified_checksums: frozenset) -> None:
    """The last check before any bytes leave. It does not trust the code that built the request.

    Rule 2 (exactly the committed bytes), rule 9 (the named interface, streamed for Anthropic,
    `store` false for OpenAI), and the refusals on instructions, second messages, earlier
    exchanges, hidden reasoning and tools.
    """
    adapter = ADAPTERS.get(request.developer)
    if adapter is None or request.developer != model.developer:
        raise Refused("refused: the request is for a different developer than the model's")
    if request.host != adapter.host or request.host not in ALLOWED_HOSTS:
        raise Refused(f"refused: {request.host!r} is not the interface the method names")
    if request.path != adapter.path_for(model.name):
        raise Refused("refused: the request's address is not the interface the method names")
    if sha256_hex(message) not in verified_checksums:
        raise Refused("refused: the message is not one of the ten committed, checked message files")
    if max_tokens > model.max_output_tokens or max_tokens < 1:
        raise Refused("refused: a length limit outside the model's own maximum")
    try:
        body = json.loads(request.body.decode("utf-8"))
    except ValueError:
        raise Refused("refused: the request body is not readable")
    forbidden = sorted(set(_keys_anywhere(body)) & NEVER_SENT)
    if forbidden:
        raise Refused("refused: the request holds what is never sent: " + ", ".join(forbidden))
    text = message.decode("utf-8")
    adapter.allowed(body, model.name, text, max_tokens)
    if text.encode("utf-8") != message:
        raise Refused("refused: the message would not reach the service byte for byte")
    names = {name.lower() for name, _ in request.headers}
    if names - {"content-type", "anthropic-version", "user-agent"}:
        raise Refused("refused: a request header that is never sent")


# ----------------------------------------------------------------------------------------
# 4. The one place that can reach the network
# ----------------------------------------------------------------------------------------

@dataclasses.dataclass
class Received:
    """Everything that came back from one exchange, before anything is made of it."""
    request_left: bool                 # False if the connection was never made
    status: int | None = None
    headers: list = dataclasses.field(default_factory=list)
    raw: bytes = b""
    broke: str | None = None           # None, or "timeout", "connection", "ended early"


class HttpsTransport:
    """The only code in this file that opens a connection. Used for real runs only.

    It talks to three named hosts and no other, over HTTPS with certificates checked, and it
    is the only place the key is turned back into text, for the one header that carries it.
    """
    reaches_network = True
    LONGEST_EXCHANGE_SECONDS = 45 * 60

    def __init__(self, key: Secret):
        self._key = key

    def exchange(self, request: Request) -> Received:
        if request.host not in ALLOWED_HOSTS:
            raise Refused(f"refused: {request.host!r} is not one of the three services")
        got = Received(request_left=False)
        connection = http.client.HTTPSConnection(request.host, 443, timeout=request.timeout_seconds,
                                                 context=ssl.create_default_context())
        chunks = []
        try:
            connection.connect()
            got.request_left = True
            headers = dict(request.headers)
            headers[request.key_header] = request.key_prefix + self._key.for_the_request_header_only()
            connection.request("POST", request.path, body=request.body, headers=headers)
            response = connection.getresponse()
            got.status = response.status
            got.headers = [[name, value] for name, value in response.getheaders()]
            started = time.monotonic()
            while True:
                chunk = response.read1(65536)
                if not chunk:
                    break
                chunks.append(chunk)
                if time.monotonic() - started > self.LONGEST_EXCHANGE_SECONDS:
                    got.broke = "timeout"
                    break
        except (TimeoutError, socket.timeout):
            got.broke = "timeout"
        except http.client.IncompleteRead as e:
            chunks.append(e.partial)
            got.broke = "ended early"
        except (OSError, http.client.HTTPException):
            got.broke = "connection"
        finally:
            connection.close()
        got.raw = b"".join(chunks)
        return got


# ----------------------------------------------------------------------------------------
# 5. The engine
# ----------------------------------------------------------------------------------------

# The seven things an attempt can be recorded as. Each is one row of the method's failures
# table. None says anything about what the reply says.
REPLY = "a reply"
CUT_OFF_LENGTH = "cut off at the length limit"
CUT_OFF_STREAM = "cut off without the signal that the reply is complete"
EMPTY = "empty"
BLOCKED = "blocked by the service"
WRONG_MODEL = "wrong model"
FAILED = "failed attempt"
NOT_MADE = "not made"


def classify(got: Received, seen: Observed, model: Model) -> str:
    """Which row of the failures table. Decided only from what the service reported.

    The order is the method's ("Which row, when a stream breaks"): a different model name
    comes first, then a length-limit stop reason, then whether the service gave its signal
    that the reply is complete, and only then whether any reply text arrived. Reasoning sent
    before the reply does not count as reply text. The words of the reply are never read
    here: `is_blank` only asks whether there are any.
    """
    if not got.request_left or got.status != 200:
        return FAILED
    if seen.reported_model is not None and seen.reported_model != model.reported_as:
        return WRONG_MODEL
    if seen.stop_kind == "length":
        return CUT_OFF_LENGTH
    if not seen.finished:
        return FAILED if seen.text.is_blank() else CUT_OFF_STREAM
    if seen.reported_model is None:
        # A complete reply that does not say which model gave it cannot be shown to be from
        # the model named. The strict reading: treat it as the wrong-model row.
        return WRONG_MODEL
    if seen.stop_kind == "blocked":
        return BLOCKED
    if seen.text.is_blank():
        return EMPTY
    return REPLY


NAME = re.compile(r"(CONSTRUCTED__)?(anthropic|google|openai)__([a-z0-9.\-]+)__q(\d\d)__asking(\d)"
                  r"__(attempt(\d\d)|not-made)\.json")


def file_name(model: Model, question: int, asking: int, attempt: int | None, constructed: bool) -> str:
    """Developer, model, question number and asking number, and no words from any reply."""
    tail = f"attempt{attempt:02d}" if attempt is not None else "not-made"
    name = (f"{CONSTRUCTED_PREFIX if constructed else ''}{model.developer}__{model.name}"
            f"__q{question:02d}__asking{asking}__{tail}.json")
    if not NAME.fullmatch(name):
        raise Refused("refused: a file name that is not in the fixed form")
    no_reply_words(name, "a file name")
    return name


@dataclasses.dataclass
class Entry:
    """One file in the reply folder, as far as the engine needs to know it."""
    name: str
    developer: str
    model: str
    question: int
    asking: int
    attempt: int | None
    outcome: str
    asked_on: datetime.date | None        # the Pacific day
    asked_at: datetime.datetime | None
    counted_usd: D
    kept_apart: bool


def read_folder(folder: pathlib.Path, constructed: bool) -> list:
    """List the attempt files already in the reply folder. Their reply text is not kept."""
    entries = []
    for sub, apart in ((folder, False), (folder / "wrong-model", True)):
        if not sub.is_dir():
            continue
        for path in sorted(sub.iterdir()):
            m = NAME.fullmatch(path.name)
            if not m:
                continue
            if bool(m.group(1)) != constructed:
                if not constructed:
                    raise Refused(f"refused: the real reply folder holds a file marked constructed: {path.name}")
                continue
            with open(path, encoding="utf-8") as f:
                record = json.load(f)
            when = record.get("asked_at_utc")
            at = datetime.datetime.fromisoformat(when) if when else None
            entries.append(Entry(
                name=path.name, developer=m.group(2), model=m.group(3), question=int(m.group(4)),
                asking=int(m.group(5)), attempt=int(m.group(7)) if m.group(7) else None,
                outcome=record["recorded_as"], asked_at=at,
                asked_on=at.astimezone(PACIFIC).date() if at else None,
                counted_usd=D(record.get("cost", {}).get("counted_toward_the_ceiling_usd", "0")),
                kept_apart=apart))
    return entries


class Engine:
    """Asks one run's models, one attempt at a time, and writes one file for each attempt."""

    def __init__(self, *, plan: Plan, run: Run, messages: dict, folder: pathlib.Path,
                 transport, world, key: Secret, mode: str, commits: dict, manifest_path: pathlib.Path):
        # The two modes cannot be mixed. A real run can only use the real transport and the
        # ruled folder; a rehearsal can only use a stand-in that cannot reach the network, and
        # a temporary folder.
        if mode == "real":
            if type(transport) is not HttpsTransport:
                raise Refused("refused: a real run must use the real transport")
            if folder.resolve() != real_reply_folder(plan).resolve():
                raise Refused(f"refused: a real reply is written only in {plan.reply_folder}")
        elif mode == "rehearsal":
            if isinstance(transport, HttpsTransport) or getattr(transport, "reaches_network", True) is not False:
                raise Refused("refused: a rehearsal must use a stand-in that cannot reach the network")
            if folder.resolve() == real_reply_folder(plan).resolve():
                raise Refused("refused: a rehearsal never writes in the real reply folder")
            if "constructed" not in folder.name.lower():
                raise Refused("refused: a rehearsal folder must have 'constructed' in its name")
        else:
            raise Refused("refused: the mode must be 'real' or 'rehearsal'")
        # Refusal: no reply is written inside a git repository. Checked before the first call.
        if inside_a_git_repository(folder):
            raise Refused(f"refused: the reply folder {folder} is inside a git repository")
        self.plan, self.run, self.messages, self.folder = plan, run, messages, folder
        self.transport, self.world, self.key, self.mode = transport, world, key, mode
        self.commits, self.manifest_path = commits, manifest_path
        self.constructed = mode == "rehearsal"
        self.verified = frozenset(sha256_hex(m) for m in messages.values())
        _keys_in_use.append(key)
        os.makedirs(folder, exist_ok=True)
        self.entries = read_folder(folder, self.constructed)

    # -- time and money ------------------------------------------------------------------

    def today(self) -> datetime.date:
        return self.world.now().astimezone(PACIFIC).date()

    def spent(self) -> D:
        """The running total for this run: every attempt on file for any of its models."""
        names = {m.name for m in self.run.models}
        return sum((e.counted_usd for e in self.entries
                    if e.developer == self.run.developer and e.model in names), D(0))

    def most_a_call_could_cost(self, model: Model, message: bytes, max_tokens: int) -> D:
        """Rule 4: a call is counted at its length limit before it is made.

        Tokens sent cannot be more than the bytes sent, plus a little for the wrapping.
        """
        replied = model.max_output_tokens if ADAPTERS[model.developer].worst_case_uses_model_maximum else max_tokens
        return ((len(message) + 64) * model.price_sent + replied * model.price_replied) / MILLION

    def check_ceiling(self, model: Model, message: bytes, max_tokens: int, a_second_asking_could_follow: bool) -> None:
        """Rule 4: stop before a call that could pass the ceiling.

        "Could pass" counts this call at its length limit and, if this is the first asking of
        the slot, the one further asking the failures table allows, at the model's own maximum.
        """
        could = self.most_a_call_could_cost(model, message, max_tokens)
        if a_second_asking_could_follow:
            could += self.most_a_call_could_cost(model, message, model.max_output_tokens)
        if self.spent() + could > self.run.ceiling_usd:
            raise RunStopped(
                f"stopped before a call that could pass the ceiling: {money(self.spent())} counted so far, "
                f"the next call and its one possible repeat could add {money(could)}, and the ceiling "
                f"for {self.run.id} is {money(self.run.ceiling_usd)}", whole_run=True)

    def check_projection(self, model: Model) -> None:
        """Rule 5: after the first round, stop if five rounds at that rate would pass the ceiling."""
        mine = [e for e in self.entries if e.model == model.name and e.developer == model.developer]
        first_round = sum((e.counted_usd for e in mine if e.asking == 1), D(0))
        others = self.spent() - sum((e.counted_usd for e in mine), D(0))
        projected = others + first_round * self.plan.askings
        say(f"  first round for {model.name} counted {money(first_round)}; {self.plan.askings} rounds at that "
            f"rate, with {money(others)} for this run's other models, come to {money(projected)} "
            f"against a ceiling of {money(self.run.ceiling_usd)}")
        if projected > self.run.ceiling_usd:
            raise RunStopped(f"stopped after the first round for {model.name}: five rounds at that rate "
                             f"would come to {money(projected)}, over the ceiling of {money(self.run.ceiling_usd)}",
                             whole_run=True)

    # -- one slot: one question in one round ----------------------------------------------

    def slot(self, model: Model, question: int, asking: int) -> list:
        return sorted((e for e in self.entries if e.developer == model.developer and e.model == model.name
                       and e.question == question and e.asking == asking),
                      key=lambda e: (e.attempt is None, e.attempt or 0))

    def next_step(self, model: Model, question: int, asking: int) -> tuple:
        """What the failures table says to do next for this slot.

        Returns ("done",), ("left for the next day",) or ("ask", length limit, whether to wait
        a minute first, whether a second asking could still follow).

        At most one further asking is ever made for a slot, whatever the second one brings,
        and never because of what a reply says. Failed attempts (no reply at all) do not count
        as askings; they are tried again up to three times in one day.
        """
        attempts = self.slot(model, question, asking)
        if any(e.outcome == NOT_MADE for e in attempts):
            return ("done",)
        answered = [e for e in attempts if e.outcome != FAILED]
        if any(e.outcome == REPLY for e in answered) or len(answered) >= 2:
            return ("done",)
        failed_today = [e for e in attempts if e.outcome == FAILED and e.asked_on == self.today()]
        if len(failed_today) >= 1 + RETRIES_AFTER_A_FAILED_ATTEMPT:
            return ("left for the next day",)
        limit = self.plan.limit_for(model)
        if answered and answered[-1].outcome == CUT_OFF_LENGTH:
            limit = model.max_output_tokens          # "Asked once more at the model's maximum"
        # PROPOSED 2026-11-18: after a reply cut off without the signal that it is complete,
        # the one further asking uses the same length limit, not the model's maximum. A broken
        # stream is not a sign that the limit was too low (the method leaves this to the script).
        wait = bool(attempts) and attempts[-1].outcome == FAILED and attempts[-1].asked_on == self.today()
        return ("ask", limit, wait, not answered)

    def fill_slot(self, model: Model, question: int, asking: int) -> bool:
        """Ask until the slot is done. False means it was left for the next day."""
        message = self.messages[f"q{question:02d}.txt"]
        while True:
            step = self.next_step(model, question, asking)
            if step[0] == "done":
                return True
            if step[0] == "left for the next day":
                return False
            _, limit, wait, second_possible = step
            if wait:
                self.world.sleep(SECONDS_BETWEEN_TRIES)
            check_day(self.run, self.today())                                    # rule 6, before every call
            self.check_ceiling(model, message, limit, second_possible)           # rule 4, before every call
            outcome = self.ask(model, question, asking, message, limit)
            if outcome == WRONG_MODEL:
                raise RunStopped(f"the service did not report the model named ({model.name}). "
                                 "The reply is kept apart and the run for this model stops at once (rule 7).")

    # -- one attempt -----------------------------------------------------------------------

    def ask(self, model: Model, question: int, asking: int, message: bytes, max_tokens: int) -> str:
        attempt = 1 + max((e.attempt or 0 for e in self.slot(model, question, asking)), default=0)
        request = build_request(model, message, max_tokens)
        check_request(request, model, message, max_tokens, self.verified)
        asked_at = self.world.now()
        got = self.transport.exchange(request)
        answered_at = self.world.now()
        adapter = ADAPTERS[model.developer]
        seen = adapter.take_apart(got.status, got.raw)
        outcome = classify(got, seen, model)

        # Rule 4: the cost, from the counts the service reports and the dated price list.
        from_counts = None
        if seen.tokens_sent is not None and seen.tokens_replied_billed is not None:
            from_counts = (seen.tokens_sent * model.price_sent
                           + seen.tokens_replied_billed * model.price_replied) / MILLION
            counted, basis = from_counts, "the token counts the service reported"
        elif not got.request_left or (got.status is not None and got.status != 200):
            # ASSUMED, NOT CHECKED: a request the service answers with an error status, or
            # that never reached it, is not charged.
            counted, basis = D(0), "no charge assumed: the service gave an error status, or was never reached"
        else:
            counted = self.most_a_call_could_cost(model, message, max_tokens)
            basis = "the service reported no full counts, so the most this call could cost is counted"

        name = file_name(model, question, asking, attempt, self.constructed)
        record = {
            "what_this_is": ("CONSTRUCTED. A rehearsal file. Nothing in it came from any model or service."
                             if self.constructed else
                             "One attempt of the sealed capture. See docs/capture/method.md in the "
                             "beyond-the-window repository."),
            "constructed": self.constructed,
            "developer": model.developer,
            "model_name_sent": model.name,
            "question_number": question,
            "asking_number": asking,
            "attempt_number": attempt,
            "recorded_as": outcome,
            "message_file": f"docs/capture/sent/q{question:02d}.txt",
            "message_sha256": sha256_hex(message),
            "message_sent": message.decode("utf-8"),
            "request": {
                "interface": adapter.interface,
                "address": f"https://{request.host}{request.path}",
                "headers_sent": [list(h) for h in request.headers]
                                + [[request.key_header, "[the key, never saved]"]],
                "headers_added_by_the_standard_library": "Host, Accept-Encoding: identity, Content-Length",
                "anthropic_version_header": ANTHROPIC_VERSION if model.developer == "anthropic" else None,
                "body_exactly_as_sent": request.body.decode("utf-8"),
                "body_sha256": sha256_hex(request.body),
                "settings_sent": {"model": model.name, "length_limit_tokens": max_tokens,
                                  "streamed": model.developer == "anthropic",
                                  "store": False if model.developer == "openai" else "not a setting of this interface"},
                "settings_not_sent": "no system message or instruction, no temperature or other sampling "
                                     "setting, no thinking or reasoning setting, no tools, no earlier exchange",
                "program_library": "none. Sent with Python's standard library (http.client), "
                                   f"Python {platform.python_version()}",
            },
            "asked_at_utc": asked_at.astimezone(datetime.timezone.utc).isoformat(),
            "asked_at_pacific": asked_at.astimezone(PACIFIC).isoformat(),
            "answer_ended_at_utc": answered_at.astimezone(datetime.timezone.utc).isoformat(),
            "service_returned": {
                "http_status": got.status,
                "headers": got.headers,
                "everything_received_in_order": got.raw.decode("utf-8", errors="replace"),
                "received_sha256": sha256_hex(got.raw),
                "connection_broke": got.broke,
                "request_reached_the_service": got.request_left,
            },
            "reply_text": seen.text.for_the_record_file_only(),
            "model_as_reported": seen.reported_model,
            "service_id_for_the_reply": seen.service_id,
            "why_the_reply_stopped": seen.stop_reason,
            "service_signalled_complete": seen.finished,
            "reasoning_was_sent_before_the_reply": seen.reasoning_seen,
            "error_type_reported": seen.error_type,
            "tokens": {"sent": seen.tokens_sent, "replied_as_billed": seen.tokens_replied_billed,
                       "reasoning": seen.tokens_reasoning},
            "reasoning_effort_reported": seen.reasoning_effort,
            "cost": {
                "from_reported_counts_usd": str(from_counts) if from_counts is not None else None,
                "counted_toward_the_ceiling_usd": str(counted),
                "basis": basis,
                "price_sent_usd_per_million": str(model.price_sent),
                "price_replied_usd_per_million": str(model.price_replied),
                "prices_read_on": self.plan.prices_read_on,
                "ceiling_usd": str(self.run.ceiling_usd),
            },
            "commits": self.commits,
        }
        self.write(name, record, apart=(outcome == WRONG_MODEL))
        self.entries.append(Entry(
            name=name, developer=model.developer, model=model.name, question=question, asking=asking,
            attempt=attempt, outcome=outcome, asked_at=asked_at, asked_on=asked_at.astimezone(PACIFIC).date(),
            counted_usd=counted, kept_apart=(outcome == WRONG_MODEL)))
        detail = f"stop reason {token(seen.stop_reason)}"
        if outcome == FAILED:
            detail = (f"http status {token(got.status)}, error {token(seen.error_type)}, "
                      f"connection {token((got.broke or 'held').replace(' ', '-'))}")
        say(f"  q{question:02d} asking {asking} attempt {attempt:02d}: {outcome} ({detail}; "
            f"limit {max_tokens}; counted {money(counted)}; run total {money(self.spent())} "
            f"of {money(self.run.ceiling_usd)})")
        return outcome

    def write(self, name: str, record: dict, apart: bool) -> pathlib.Path:
        """Rule 8: write the file before the next message is sent, and make it read-only.

        The file is created new and never opened again for writing; an existing name is an
        error, so nothing is ever overwritten. Refusal "delete a file": nothing in this script
        removes, renames or empties a file.
        """
        folder = self.folder / "wrong-model" if apart else self.folder
        if inside_a_git_repository(folder):
            raise Refused(f"refused: {folder} is inside a git repository")
        os.makedirs(folder, exist_ok=True)
        text = json.dumps(record, ensure_ascii=False, indent=1)
        if self.key.appears_in(text):
            # "The key is never saved." If a service ever sent the key back, it is taken out.
            text = self.key.removed_from(text)
            text = text[:-1].rstrip() + ',\n "key_was_removed_from_this_record": true\n}'
        path = folder / name
        handle = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)
        with os.fdopen(handle, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(path, 0o444)
        return path

    # -- one model, and the whole run --------------------------------------------------------

    def run_model(self, model: Model) -> None:
        check_day(self.run, self.today())
        if any(e.kept_apart and e.model == model.name and e.developer == model.developer for e in self.entries):
            raise RunStopped(f"a reply from a different model is on file for {model.name}. Its run stays "
                             "stopped until John rules.")
        say(f"{model.name}: {self.plan.askings} rounds of {self.plan.questions} questions")
        for asking in range(1, self.plan.askings + 1):
            if asking == 2 and any(self.next_step(model, q, a)[0] != "done"
                                   for a in range(2, self.plan.askings + 1)
                                   for q in range(1, self.plan.questions + 1)):
                self.check_projection(model)                                       # rule 5
            for question in range(1, self.plan.questions + 1):
                if not self.fill_slot(model, question, asking):
                    raise RunStopped(
                        f"question {question} in round {asking} for {model.name} brought no reply after "
                        f"{1 + RETRIES_AFTER_A_FAILED_ATTEMPT} tries and is left for the next day. A round "
                        "finishes before the next starts, so this model's run stops for now.")
            say(f" round {asking} for {model.name} is complete")
            self.say_faults(model, asking)                                          # rule 10

    def run_all(self, only_model: str | None = None) -> bool:
        """Run every model of the run in turn. Returns True if nothing stopped early."""
        clean = True
        try:
            for model in self.run.models:
                if only_model and model.name != only_model:
                    continue
                try:
                    self.run_model(model)
                except RunStopped as e:
                    clean = False
                    say(f"STOPPED: {e}")
                    if e.whole_run:
                        break                      # the ceiling is for the whole run
        finally:
            write_manifest(self.folder, self.manifest_path, self.constructed)      # rule 8
            say(f"run total counted: {money(self.spent())} of {money(self.run.ceiling_usd)}")
        return clean

    def record_not_made(self) -> int:
        """After the last safe day: record every asking that was never completed as not made."""
        if self.today() <= self.run.last_safe_day:
            raise Refused("askings are recorded as not made only after the last safe day")
        written = 0
        for model in self.run.models:
            for asking in range(1, self.plan.askings + 1):
                for question in range(1, self.plan.questions + 1):
                    if self.next_step(model, question, asking)[0] == "done":
                        continue
                    name = file_name(model, question, asking, None, self.constructed)
                    now = self.world.now()
                    self.write(name, {
                        "what_this_is": ("CONSTRUCTED. A rehearsal file." if self.constructed else
                                         "An asking of the sealed capture that was not made."),
                        "constructed": self.constructed, "developer": model.developer,
                        "model_name_sent": model.name, "question_number": question,
                        "asking_number": asking, "recorded_as": NOT_MADE,
                        "why": f"not completed by the last safe day, {self.run.last_safe_day}",
                        "asked_at_utc": None,
                        "recorded_at_utc": now.astimezone(datetime.timezone.utc).isoformat(),
                        "cost": {"counted_toward_the_ceiling_usd": "0"}, "commits": self.commits}, apart=False)
                    self.entries.append(Entry(name=name, developer=model.developer, model=model.name,
                                              question=question, asking=asking, attempt=None, outcome=NOT_MADE,
                                              asked_on=None, asked_at=None, counted_usd=D(0), kept_apart=False))
                    written += 1
        write_manifest(self.folder, self.manifest_path, self.constructed)
        return written

    def say_faults(self, model: Model, asking: int) -> None:
        lines = fault_lines(self.folder, self.plan.very_short_words, self.constructed,
                            developer=model.developer, model=model.name, asking=asking)
        say(f" fault check for round {asking}: {len(lines)} file(s) flagged"
            + (" (name, fault, count; no words of any reply are shown)" if lines else ""))
        for line in lines:
            say("   " + line)


# ----------------------------------------------------------------------------------------
# 6. The fault list, the list of names and checksums, and the commands
# ----------------------------------------------------------------------------------------

def fault_lines(folder: pathlib.Path, very_short_words: int, constructed: bool, *,
                developer: str | None = None, model: str | None = None, asking: int | None = None) -> list:
    """Rule 10: list faulty reply files by name, fault and count, and never any words.

    A file is listed if its reply is empty, ended mid-reply (the stop reason is the length
    limit, or the reply ended after some text without the service's signal that it was
    complete), or is very short (fewer words than the threshold in the plan). A failed
    attempt, which brought no reply, is not a reply file and is not listed here.
    """
    lines = []
    for sub in (folder, folder / "wrong-model"):
        if not sub.is_dir():
            continue
        for path in sorted(sub.iterdir()):
            m = NAME.fullmatch(path.name)
            if not m or bool(m.group(1)) != constructed or not m.group(7):
                continue
            if (developer and m.group(2) != developer) or (model and m.group(3) != model) \
                    or (asking and int(m.group(5)) != asking):
                continue
            with open(path, encoding="utf-8") as f:
                record = json.load(f)
            outcome = record["recorded_as"]
            if outcome in (FAILED, NOT_MADE):
                continue
            words = Sealed(str(record.get("reply_text") or "")).word_count()      # counted, never shown
            reason = token(record.get("why_the_reply_stopped"))
            if outcome == CUT_OFF_LENGTH:
                fault = f"ended mid-reply | stop reason {reason}, {words} words"
            elif outcome == CUT_OFF_STREAM:
                fault = f"ended mid-reply | no signal that the reply was complete, {words} words"
            elif words == 0:
                fault = f"empty | 0 words, stop reason {reason}"
            elif words < very_short_words:
                fault = f"very short | {words} words (fewer than {very_short_words})"
            else:
                continue
            line = f"{path.name} | {fault}"
            no_reply_words(line, "the fault list")
            lines.append(line)
    return lines


def write_manifest(folder: pathlib.Path, manifest_path: pathlib.Path, constructed: bool) -> int:
    """Rule 8: the list of names and checksums, written at the end. Names and checksums only."""
    rows = []
    for sub, prefix in ((folder, ""), (folder / "wrong-model", "wrong-model/")):
        if not sub.is_dir():
            continue
        for path in sorted(sub.iterdir()):
            m = NAME.fullmatch(path.name)
            if m and bool(m.group(1)) == constructed:
                rows.append(f"{sha256_hex(path.read_bytes())}  {prefix}{path.name}")
    head = ["# The sealed capture: the list of file names and checksums", ""]
    if constructed:
        head += ["**CONSTRUCTED.** Written by the rehearsal. No file listed here came from any model.", ""]
    head += ["Written by `capture/capture.py`. One line for each file in the reply folder, which is "
             "outside every repository: its SHA-256 checksum, then its name. Nothing else is here, "
             "and no word of any reply.", "", "```text"]
    text = "\n".join(head + rows + ["```", ""])
    no_reply_words(text, "the list of names and checksums")
    os.makedirs(manifest_path.parent, exist_ok=True)
    manifest_path.write_text(text, encoding="utf-8")
    return len(rows)


def check_manifest(folder: pathlib.Path, manifest_path: pathlib.Path) -> list:
    """Compare the reply folder with the committed list. Returns the problems, by name only."""
    listed = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"([0-9a-f]{64})  (\S+)", line)
        if m:
            listed[m.group(2)] = m.group(1)
    problems = []
    for name, checksum in sorted(listed.items()):
        path = folder / name
        if not path.exists():
            problems.append(f"{name}: listed, and missing from the folder")
        elif sha256_hex(path.read_bytes()) != checksum:
            problems.append(f"{name}: differs from its listed checksum")
    return problems


class RealWorld:
    def now(self) -> datetime.datetime:
        return datetime.datetime.now(datetime.timezone.utc)

    def sleep(self, seconds: int) -> None:
        time.sleep(seconds)


def read_key(run: Run) -> Secret:
    """Rule 1. The key comes from this project's own environment variable and nowhere else.

    The variable's name is this project's alone (it starts BTW_CAPTURE_), so a key that
    another project left in the shell under a common name such as ANTHROPIC_API_KEY is never
    picked up. The variable is taken out of this program's environment as soon as it is read,
    so the one other program this script starts afterwards (git, to check that the reply folder
    is outside every repository) cannot be handed it.
    """
    value = os.environ.pop(run.key_variable, "").strip()
    if not value:
        raise Refused(f"the environment variable {run.key_variable} is not set. This script reads "
                      "the key from it and from nowhere else.")
    return Secret(value)


def show(paths: Paths, plan: Plan, run: Run, today: datetime.date, all_bodies: bool) -> bool:
    """Print exactly what a run would send, to which models, how often and at what cost. Then stop."""
    say(f"WHAT A RUN OF {run.id} WOULD DO. Nothing is sent by this command.")
    say(f"today (Pacific): {today}; withdrawal date: {run.withdrawal_date}; last safe day: {run.last_safe_day}")
    say(f"replies would be written in: {plan.reply_folder}")
    say("")
    say("Checks made before a real run:")
    results, learned = start_checks(paths, plan, run, today, real_reply_folder(plan))
    for label, ok, detail in results:
        say(f"  [{'pass' if ok else 'FAIL'}] {label}" + (f"\n         {detail}" if detail else ""))
    say(f"  [{'pass' if os.environ.get(run.key_variable) else 'FAIL'}] the environment variable "
        f"{run.key_variable} is set (its value is not read or shown here)")
    messages = learned.get("messages")
    if not messages:
        say("")
        say("The message files did not pass their check, so no request is shown.")
        return False
    say("")
    say("The ten messages, exactly as committed:")
    for name, data in messages.items():
        say(f"  {name}  {len(data)} bytes  sha256 {sha256_hex(data)}")
    say("")
    total_estimate, total_worst = D(0), D(0)
    exchanges = plan.questions * plan.askings
    for model in run.models:
        adapter = ADAPTERS[model.developer]
        limit = plan.limit_for(model)
        say(f"MODEL {model.name}")
        say(f"  interface: {adapter.interface}")
        say(f"  exchanges: {plan.questions} messages x {plan.askings} askings = {exchanges}, each a new exchange; "
            "more only where the failures table asks once more")
        say(f"  length limit sent: {limit} tokens (the model's own maximum is {model.max_output_tokens})")
        shown = list(messages.items()) if all_bodies else list(messages.items())[:1]
        for name, data in shown:
            request = build_request(model, data, limit)
            check_request(request, model, data, limit, frozenset(sha256_hex(m) for m in messages.values()))
            say(f"  request for {name}:")
            say(f"    POST https://{request.host}{request.path}")
            for header, value in request.headers:
                say(f"    {header}: {value}")
            say(f"    {request.key_header}: {request.key_prefix}[the key from {run.key_variable}, not shown]")
            say("    body, exactly:")
            say("    " + request.body.decode("utf-8"))
        if not all_bodies:
            say("  (the other nine requests differ only in the message; --all-bodies prints them)")
        estimate = (exchanges * plan.estimate_sent_tokens * model.price_sent
                    + exchanges * model.estimate_reply_tokens * model.price_replied) / MILLION
        engine_free_worst = sum(((len(d) + 64) * model.price_sent
                                 + (model.max_output_tokens if adapter.worst_case_uses_model_maximum else limit)
                                 * model.price_replied) / MILLION for d in messages.values()) * plan.askings
        total_estimate += estimate
        total_worst += engine_free_worst
        say(f"  estimated cost: {money(estimate)} ({plan.estimate_sent_tokens} tokens sent and "
            f"{model.estimate_reply_tokens} replied for each exchange, the guesses in cost-and-terms.md, "
            f"at ${model.price_sent} and ${model.price_replied} a million)")
        say(f"  if every reply ran to its limit: {money(engine_free_worst)}")
        say("")
    say(f"RUN {run.id}: estimated {money(total_estimate)}; with one fifth added for repeats "
        f"{money(total_estimate * D('1.2'))}; if every reply ran to its limit {money(total_worst)}; "
        f"ceiling {money(run.ceiling_usd)} (the script stops before a call that could pass it)")
    return all(ok for _, ok, _ in results)


def find_repo() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent.parent


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="The sealed capture. See capture/README.md.")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("show", help="print exactly what a run would send and cost, then stop")
    p.add_argument("--run", required=True)
    p.add_argument("--all-bodies", action="store_true")
    p = sub.add_parser("run", help="ask. Needs John's go in the spending record and the key in the environment")
    p.add_argument("--run", required=True)
    p.add_argument("--model", help="ask only this model of the run")
    p = sub.add_parser("record-not-made", help="after the last safe day, record unfinished askings as not made")
    p.add_argument("--run", required=True)
    sub.add_parser("faults", help="list faulty reply files by name, fault and count, never their words")
    sub.add_parser("manifest", help="write the list of file names and checksums")
    sub.add_parser("check-manifest", help="compare the reply folder with the committed list")
    args = parser.parse_args(argv)

    paths = Paths(find_repo())
    plan = load_plan(paths.plan)
    folder = real_reply_folder(plan)
    world = RealWorld()
    today = world.now().astimezone(PACIFIC).date()
    try:
        if args.command == "show":
            show(paths, plan, plan.run(args.run), today, args.all_bodies)
            return 0
        if args.command == "faults":
            lines = fault_lines(folder, plan.very_short_words, False) if folder.is_dir() else []
            say(f"{len(lines)} file(s) flagged (name, fault, count; no words of any reply are shown)")
            for line in lines:
                say(line)
            return 0
        if args.command == "manifest":
            if inside_a_git_repository(folder) or not folder.is_dir():
                raise Refused("the reply folder does not exist, or is inside a git repository")
            say(f"{write_manifest(folder, paths.manifest, False)} file(s) listed in {paths.manifest}")
            return 0
        if args.command == "check-manifest":
            problems = check_manifest(folder, paths.manifest)
            for line in problems:
                say(line)
            say("the folder matches the list" if not problems else f"{len(problems)} problem(s)")
            return 1 if problems else 0

        run = plan.run(args.run)
        results, learned = start_checks(paths, plan, run, today, folder)
        failed = [(label, detail) for label, ok, detail in results if not ok]
        if args.command == "record-not-made":
            # Only the checks that still make sense after the last safe day.
            failed = [(l, d) for l, d in failed if not l.startswith("today is not after")]
        if failed:
            say("REFUSED. Nothing was asked. These checks did not pass:")
            for label, detail in failed:
                say(f"  {label}\n    {detail}")
            return 2
        if args.command == "record-not-made":
            engine = Engine(plan=plan, run=run, messages=learned["messages"], folder=folder,
                            transport=HttpsTransport(Secret("")), world=world, key=Secret(""),
                            mode="real", commits=learned["commits"], manifest_path=paths.manifest)
            say(f"{engine.record_not_made()} asking(s) recorded as not made")
            return 0
        if args.model and args.model not in {m.name for m in run.models}:
            raise Refused(f"{args.model!r} is not a model of {run.id}")
        key = read_key(run)                    # the last thing before the first call
        engine = Engine(plan=plan, run=run, messages=learned["messages"], folder=folder,
                        transport=HttpsTransport(key), world=world, key=key, mode="real",
                        commits=learned["commits"], manifest_path=paths.manifest)
        return 0 if engine.run_all(args.model) else 3
    except Refused as e:
        say(f"REFUSED. {e}")
        return 2
    except Exception as e:      # noqa: BLE001
        # The error's own message is not printed, in case it holds text from a file it was reading.
        say(f"STOPPED by an unexpected error of the kind {type(e).__name__}. Files already written stay. "
            "Nothing was deleted. Run the same command again to carry on, or ask a session to look.")
        return 4


if __name__ == "__main__":
    sys.exit(main())
