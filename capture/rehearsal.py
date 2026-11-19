#!/usr/bin/env python3
"""The rehearsal of the sealed capture script (method, script rule 11).

Written 2026-11-18 by Claude (Fable 5.2), an AI model.

It calls no service. Every "reply" in it is CONSTRUCTED: made up here, marked with that word
in its own text, in its file name and in its record, and written only in a temporary folder
that is removed at the end. Nobody should be able to mistake one for a real answer.

What it does:

  1. Before the script is even loaded, it replaces every way Python has of opening a network
     connection with a tripwire that raises an error and counts the attempt. If any code path
     of the script tried to reach the network, the rehearsal would fail loudly. It then proves
     the tripwire works, once against this machine's own address and once against the
     script's real network code, which is stopped before any connection is made.
  2. It builds a small constructed repository and a constructed reply folder, both temporary.
  3. It runs the script's real engine against a local stand-in for each developer's service,
     once for every row of the method's failures table and every case rule 11 lists, and
     checks what was written and what was asked next.
  4. It exercises every refusal and every start check.

Run it from anywhere:  python3 -I capture/rehearsal.py
It exits 0 only if every check passed, and its last line then names the checksums of the
script and the plan it tested. The script refuses a real run unless that line, for the script
and plan as they then stand, is saved in capture/rehearsal-result.txt.
"""
import socket
import ssl

# ----- 1. the tripwire, installed before anything else is loaded --------------------------
TRIPPED = []


class TripwireHit(RuntimeError):
    pass


def _tripwire(*args, **kwargs):
    TRIPPED.append(repr(args[:2])[:80])
    raise TripwireHit("TRIPWIRE: something tried to open a network connection during the rehearsal")


socket.create_connection = _tripwire
socket.getaddrinfo = _tripwire
socket.socket.connect = _tripwire
socket.socket.connect_ex = _tripwire
ssl.SSLSocket.connect = _tripwire

import ast                    # noqa: E402
import dataclasses            # noqa: E402
import datetime               # noqa: E402
import decimal                # noqa: E402
import importlib.util         # noqa: E402
import json                   # noqa: E402
import os                     # noqa: E402
import pathlib                # noqa: E402
import re                     # noqa: E402
import shutil                 # noqa: E402
import stat                   # noqa: E402
import subprocess             # noqa: E402
import sys                    # noqa: E402
import tempfile               # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
REAL_REPO = HERE.parent
spec = importlib.util.spec_from_file_location("capture", HERE / "capture.py")
capture = importlib.util.module_from_spec(spec)
sys.modules["capture"] = capture
spec.loader.exec_module(capture)

D = decimal.Decimal
MARK = "STANDINTEXT"          # a word that is in every constructed reply and nowhere else
CONSTRUCTED_KEY = "CONSTRUCTED-not-a-key-0000-for-the-rehearsal-only"
OTHER_PROJECTS_KEY = "CONSTRUCTED-some-other-projects-key-never-used"

SAID = []                     # every line the script would have printed
capture._sink = SAID.append

FAILURES = []
CHECKS = 0


def check(condition, what):
    global CHECKS
    CHECKS += 1
    print(f"    {'pass' if condition else 'FAIL'}  {what}")
    if not condition:
        FAILURES.append(what)


def case(title):
    print(f"\n{title}")


def refuses(fn, what, expect=None):
    try:
        fn()
    except capture.Refused as e:
        check(expect is None or expect in str(e), f"refused: {what}")
        return str(e)
    check(False, f"refused: {what} (it was NOT refused)")
    return ""


# ----- constructed text ----------------------------------------------------------------

def message_text(n):
    return f"CONSTRUCTED message q{n:02d}. Not a real question. Made for the rehearsal only."


LONG = ("CONSTRUCTED reply, not from any model. {mark} number {n}: filler for the rehearsal of the "
        "sealed capture script, long enough to pass the threshold of twenty words without being flagged.")
DECLINE = ("CONSTRUCTED reply, not from any model. {mark}: this stand-in plays a reply that declines. "
           "It says it would rather not answer the constructed question and gives a constructed reason.")
SHORT = "CONSTRUCTED {mark}: no."


class Clock:
    """A made-up clock. The rehearsal never waits; a "sleep" only moves this clock on."""

    def __init__(self, start):
        self.t = start
        self.sleeps = []

    def now(self):
        self.t += datetime.timedelta(milliseconds=100)
        return self.t

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.t += datetime.timedelta(seconds=seconds)


def pacific(y, m, d, hh=10, mm=0):
    return datetime.datetime(y, m, d, hh, mm, tzinfo=capture.PACIFIC).astimezone(datetime.timezone.utc)


# ----- the stand-in for the three services -------------------------------------------------

def sse(*events):
    return "".join(f"event: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in events).encode()


def a_start(model):
    return {"type": "message_start", "message": {
        "id": "msg_CONSTRUCTED", "type": "message", "role": "assistant", "model": model, "content": [],
        "stop_reason": None, "usage": {"input_tokens": 210, "output_tokens": 1}}}


A_BLOCK = {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}
A_BLOCK_STOP = {"type": "content_block_stop", "index": 0}
A_STOP = {"type": "message_stop"}
A_PING = {"type": "ping"}
A_ERROR = {"type": "error", "error": {"type": "overloaded_error", "message": "CONSTRUCTED overloaded"}}
A_THINK = [{"type": "content_block_start", "index": 0, "content_block": {"type": "thinking", "thinking": ""}},
           {"type": "content_block_delta", "index": 0,
            "delta": {"type": "thinking_delta", "thinking": "CONSTRUCTED reasoning, not from any model"}}]


def a_text(text):
    half = len(text) // 2
    return [{"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": part}}
            for part in (text[:half], text[half:]) if part]


def a_end(stop, out=60):
    return {"type": "message_delta", "delta": {"stop_reason": stop, "stop_sequence": None},
            "usage": {"output_tokens": out}}


def anthropic_wire(spec, model, text):
    kind = spec["kind"]
    ok = lambda *events, broke=None: capture.Received(   # noqa: E731
        request_left=True, status=200, headers=[["content-type", "text/event-stream"],
                                                 ["request-id", "req_CONSTRUCTED"]] + spec.get("headers", []),
        raw=sse(*events), broke=broke)
    whole = [a_start(model), A_BLOCK, A_PING, *a_text(text), A_BLOCK_STOP]
    if kind in ("ok", "text"):
        return ok(*whole, a_end("end_turn", spec.get("out", 60)), A_STOP)
    if kind == "http":
        body = {"type": "error", "error": {"type": spec["error"], "message": "CONSTRUCTED error"},
                "request_id": "req_CONSTRUCTED"}
        return capture.Received(request_left=True, status=spec["status"], headers=[], raw=json.dumps(body).encode())
    if kind == "noconnect":
        return capture.Received(request_left=False, broke="connection")
    if kind == "length":
        return ok(*whole, a_end("max_tokens", 32000), A_STOP)
    if kind == "length_empty":
        return ok(a_start(model), a_end("max_tokens", 32000), A_STOP)
    if kind == "empty":
        return ok(a_start(model), a_end("end_turn", 2), A_STOP)
    if kind == "blocked":
        return ok(a_start(model), a_end("refusal", 1), A_STOP)
    if kind == "wrongmodel":
        return ok(a_start("claude-CONSTRUCTED-other-model"), A_BLOCK, *a_text(text), A_BLOCK_STOP,
                  a_end("end_turn"), A_STOP)
    # the cases under "Which row, when a stream breaks"
    if kind == "nosignal":                      # some text, then the stream simply ends
        return ok(a_start(model), A_BLOCK, *a_text(text))
    if kind == "error_after_text":
        return ok(a_start(model), A_BLOCK, *a_text(text), A_ERROR)
    if kind == "timeout_after_text":
        return ok(a_start(model), A_BLOCK, *a_text(text), broke="timeout")
    if kind == "error_before_text":
        return ok(a_start(model), A_ERROR)
    if kind == "closed_before_text":
        return ok(a_start(model), A_BLOCK, broke="ended early")
    if kind == "wrongmodel_break":
        return ok(a_start("claude-CONSTRUCTED-other-model"), A_BLOCK, *a_text(text), broke="connection")
    if kind == "length_break_text":
        return ok(a_start(model), A_BLOCK, *a_text(text), A_BLOCK_STOP, a_end("max_tokens", 32000), broke="connection")
    if kind == "length_break_notext":
        return ok(a_start(model), a_end("max_tokens", 32000), broke="timeout")
    if kind == "reasoning_break":
        return ok(a_start(model), *A_THINK, broke="connection")
    raise AssertionError(kind)


def google_wire(spec, model, text):
    kind = spec["kind"]
    usage = {"promptTokenCount": 200, "candidatesTokenCount": 60, "thoughtsTokenCount": 900, "totalTokenCount": 1160}

    def ok(body):
        return capture.Received(request_left=True, status=200, headers=[], raw=json.dumps(body).encode())

    def reply(parts, finish, reported=model):
        cand = {"content": {"role": "model", "parts": parts}, "finishReason": finish, "index": 0}
        return {"candidates": [cand], "usageMetadata": usage, "modelVersion": reported, "responseId": "CONSTRUCTED-id"}
    if kind in ("ok", "text"):
        return ok(reply([{"text": text}], "STOP"))
    if kind == "http":
        return capture.Received(request_left=True, status=spec["status"], headers=[], raw=json.dumps(
            {"error": {"code": spec["status"], "message": "CONSTRUCTED error", "status": spec["error"]}}).encode())
    if kind == "length_empty":                  # the limit reached while thinking: no text at all
        return ok(reply([], "MAX_TOKENS"))
    if kind == "blocked":                       # the message itself was blocked
        return ok({"promptFeedback": {"blockReason": "PROHIBITED_CONTENT"}, "usageMetadata": {"promptTokenCount": 200},
                   "modelVersion": model, "responseId": "CONSTRUCTED-id"})
    if kind == "blocked_reply":
        return ok(reply([], "SAFETY"))
    if kind == "empty":
        return ok(reply([], "STOP"))
    if kind == "wrongmodel":
        return ok(reply([{"text": text}], "STOP", reported="gemini-CONSTRUCTED-other-model"))
    if kind == "garbled":                       # the connection breaks part way through the body
        return capture.Received(request_left=True, status=200, headers=[], raw=b'{"candidates": [{"conte', broke="ended early")
    raise AssertionError(kind)


def openai_wire(spec, model, text):
    kind = spec["kind"]

    def ok(body):
        return capture.Received(request_left=True, status=200, headers=[], raw=json.dumps(body).encode())

    def reply(content, state="completed", reason=None, reported=model):
        output = [{"type": "reasoning", "id": "rs_CONSTRUCTED", "summary": []}]
        if content is not None:
            output.append({"type": "message", "id": "msg_CONSTRUCTED", "role": "assistant", "status": "completed",
                           "content": content})
        return {"id": "resp_CONSTRUCTED", "object": "response", "status": state, "model": reported,
                "incomplete_details": {"reason": reason} if reason else None, "output": output,
                "usage": {"input_tokens": 200, "output_tokens": 700, "total_tokens": 900,
                          "output_tokens_details": {"reasoning_tokens": 640}},
                "reasoning": {"effort": "medium", "summary": None}, "store": False}
    if kind in ("ok", "text"):
        return ok(reply([{"type": "output_text", "text": text, "annotations": []}]))
    if kind == "http":
        return capture.Received(request_left=True, status=spec["status"], headers=[], raw=json.dumps(
            {"error": {"message": "CONSTRUCTED error", "type": spec["error"], "code": None}}).encode())
    if kind == "length_empty":
        return ok(reply(None, "incomplete", "max_output_tokens"))
    if kind == "blocked":
        return ok(reply(None, "incomplete", "content_filter"))
    if kind == "refusal_part":                  # the service files the model's words under "refusal"
        return ok(reply([{"type": "refusal", "refusal": text}]))
    if kind == "empty":
        return ok(reply([]))
    if kind == "wrongmodel":
        return ok(reply([{"type": "output_text", "text": text, "annotations": []}], reported="gpt-CONSTRUCTED-other"))
    raise AssertionError(kind)


WIRES = {"anthropic": anthropic_wire, "google": google_wire, "openai": openai_wire}


class StandIn:
    """A local stand-in for a developer's service. It opens nothing and returns constructed bytes.

    `faults` maps a question number to the list of things the "service" does for that
    question's next calls, in order. After the list runs out, every call gets an ordinary
    constructed reply.
    """
    reaches_network = False

    def __init__(self, faults=None, out_tokens=60):
        self.faults = {q: list(specs) for q, specs in (faults or {}).items()}
        self.calls = []
        self.out_tokens = out_tokens

    def exchange(self, request):
        body = json.loads(request.body)
        sent = {"anthropic": lambda: body["messages"][0]["content"],
                "google": lambda: body["contents"][0]["parts"][0]["text"],
                "openai": lambda: body["input"]}[request.developer]()
        question = int(re.search(r"CONSTRUCTED message q(\d\d)", sent).group(1))
        self.calls.append((question, request))
        queue = self.faults.get(question) or []
        spec = queue.pop(0) if queue else {"kind": "ok", "out": self.out_tokens}
        text = spec.get("text", LONG).format(mark=MARK, n=len(self.calls))
        return WIRES[request.developer](spec, request.model, text)


# ----- the constructed repository ---------------------------------------------------------

def git(repo, *args):
    done = subprocess.run(["git", "-C", str(repo), "-c", "user.name=rehearsal", "-c", "user.email=rehearsal@localhost",
                           "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null", *args],
                          capture_output=True, text=True)
    assert done.returncode == 0, done.stderr
    return done.stdout


def go_block(run, sums_checksum, ceiling=None, words=None):
    ceiling = ceiling or f"{run.ceiling_usd}"
    words = words or f"CONSTRUCTED go for {run.id}, up to ${ceiling}"
    return (f"\n> {words}\n\n```sealed-capture-go\nrun = \"{run.id}\"\nceiling_usd = \"{ceiling}\"\n"
            f"johns_words = \"{words}\"\nmessages_sha256 = \"{sums_checksum}\"\n```\n")


def make_repo(root, plan_text=None, spending=True):
    """A constructed repository: the real script and plan, the two real capture documents the
    plan is checked against, constructed messages, and a constructed spending record."""
    repo = root / "constructed-repository"
    (repo / "capture").mkdir(parents=True)
    (repo / "docs" / "capture" / "sent").mkdir(parents=True)
    shutil.copy(HERE / "capture.py", repo / "capture" / "capture.py")
    (repo / "capture" / "plan.toml").write_text(plan_text or (HERE / "plan.toml").read_text(), encoding="utf-8")
    for name in ("what-john-needs-to-do.md", "cost-and-terms.md"):
        shutil.copy(REAL_REPO / "docs" / "capture" / name, repo / "docs" / "capture" / name)
    sums = ""
    for n in range(1, 11):
        data = message_text(n).encode("utf-8")
        (repo / "docs" / "capture" / "sent" / f"q{n:02d}.txt").write_bytes(data)
        sums += f"{capture.sha256_hex(data)}  q{n:02d}.txt\n"
    (repo / "docs" / "capture" / "sent" / "SHA256SUMS").write_text(sums, encoding="utf-8")
    plan = capture.load_plan(repo / "capture" / "plan.toml")
    if spending:
        record = "# CONSTRUCTED spending record, for the rehearsal only\n"
        for run in plan.runs:
            record += go_block(run, capture.sha256_hex(sums.encode()))
        (repo / "docs" / "spending-record.md").write_text(record, encoding="utf-8")
    (repo / "capture" / "rehearsal-result.txt").write_text(
        "CONSTRUCTED result, so that the start check can be exercised\n"
        f"REHEARSAL PASSED 2026-11-18 capture.py={capture.sha256_hex((HERE / 'capture.py').read_bytes())} "
        f"plan.toml={capture.sha256_hex((repo / 'capture' / 'plan.toml').read_bytes())}\n", encoding="utf-8")
    git(repo, "init", "-q")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "CONSTRUCTED repository for the rehearsal")
    return repo


def variant(root, base, name, edit, commit=True):
    """A copy of the constructed repository with one thing changed."""
    repo = root / name / "constructed-repository"
    shutil.copytree(base, repo)
    edit(repo)
    if commit:
        git(repo, "add", "-A")
        git(repo, "commit", "-q", "--allow-empty", "-m", "CONSTRUCTED change for the rehearsal")
    return repo


def records(folder):
    out = []
    for sub in (folder, folder / "wrong-model"):
        if sub.is_dir():
            for path in sorted(sub.iterdir()):
                if path.suffix == ".json":
                    out.append((path, json.loads(path.read_text(encoding="utf-8"))))
    return out


class Bench:
    """Everything a case needs: the constructed repository, the plan, and fresh reply folders."""

    def __init__(self, root):
        self.root = root
        self.repo = make_repo(root)
        self.paths = capture.Paths(self.repo)
        self.plan = capture.load_plan(self.paths.plan)
        self.n = 0
        results, learned = capture.start_checks(self.paths, self.plan, self.plan.run("anthropic-2026-11-30"),
                                                datetime.date(2026, 11, 27), self.folder())
        self.start_results = results
        self.messages, self.commits = learned["messages"], learned["commits"]

    def folder(self):
        self.n += 1
        return self.root / f"constructed-replies-{self.n:03d}"

    def engine(self, run_id="anthropic-2026-11-30", faults=None, folder=None, clock=None, plan=None,
               out_tokens=60, standin=None):
        plan = plan or self.plan
        folder = folder or self.folder()
        clock = clock or Clock(pacific(2026, 11, 27))
        standin = standin or StandIn(faults, out_tokens)
        eng = capture.Engine(plan=plan, run=plan.run(run_id), messages=self.messages, folder=folder,
                             transport=standin, world=clock, key=capture.Secret(CONSTRUCTED_KEY), mode="rehearsal",
                             commits=self.commits, manifest_path=folder.parent / f"{folder.name}-manifest.md")
        return eng, standin, clock, folder

    def plan_with(self, old, new):
        text = (HERE / "plan.toml").read_text(encoding="utf-8")
        assert old in text
        path = self.root / f"constructed-plan-{self.n}-{len(new)}.toml"
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        return capture.load_plan(path)


def slot(folder, q, asking=1, model=None):
    return [(p, r) for p, r in records(folder) if r["question_number"] == q and r["asking_number"] == asking
            and (model is None or r["model_name_sent"] == model)]


def outcomes(folder, q, asking=1, model=None):
    return [r["recorded_as"] for _, r in slot(folder, q, asking, model)]


def limits(standin, q):
    return [req.max_tokens for question, req in standin.calls if question == q]


# ==========================================================================================

def part_tripwire():
    case("TRIPWIRE. No code path may reach the network (rule 11: the rehearsal calls no service)")
    before = len(TRIPPED)
    try:
        socket.create_connection(("127.0.0.1", 9), timeout=1)
        check(False, "the tripwire stops a connection to this machine's own address")
    except TripwireHit:
        check(True, "the tripwire stops a connection to this machine's own address")
    try:
        sock = socket.socket()
        try:
            sock.connect(("127.0.0.1", 9))
            check(False, "the tripwire stops a bare socket connecting")
        finally:
            sock.close()
    except TripwireHit:
        check(True, "the tripwire stops a bare socket connecting")
    # The script's real network code, with a constructed key, a constructed message. The
    # tripwire stops it before any connection is made; nothing leaves this machine.
    model = capture.load_plan(HERE / "plan.toml").run("anthropic-2026-11-30").models[0]
    request = capture.build_request(model, message_text(1).encode(), 32000)
    try:
        capture.HttpsTransport(capture.Secret(CONSTRUCTED_KEY)).exchange(request)
        check(False, "the script's real network code is caught by the tripwire")
    except TripwireHit:
        check(True, "the script's real network code is caught by the tripwire before it connects")
    check(len(TRIPPED) - before == 3, "exactly these three deliberate attempts were counted")
    return len(TRIPPED)


def part_source():
    case("THE SOURCE. What the script's code can and cannot do, read from its syntax tree")
    source = (HERE / "capture.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported |= {a.name for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module)
    allowed = {"__future__", "argparse", "dataclasses", "datetime", "decimal", "hashlib", "http.client", "json", "os",
               "pathlib", "platform", "re", "socket", "ssl", "subprocess", "sys", "time", "tomllib", "zoneinfo"}
    check(imported <= allowed, f"only the Python standard library is imported ({len(imported)} modules, none else)")
    check(not imported & {"urllib", "urllib.request", "shutil", "requests", "httpx", "anthropic", "openai"},
          "no other way to reach the network, and no module for removing folders, is imported")
    calls = [ast.unparse(n.func) for n in ast.walk(tree) if isinstance(n, ast.Call)]
    deleting = [c for c in calls if c in ("os.remove", "os.unlink", "os.rmdir", "os.rename", "os.replace",
                                          "os.truncate", "os.removedirs")
                or c.endswith((".unlink", ".rmdir", ".rename", ".truncate", ".rmtree"))]
    check(deleting == [], "refusal 'delete a file': no call that removes, renames or empties a file exists")
    check(calls.count("http.client.HTTPSConnection") == 1 and not any("create_connection" in c or "urlopen" in c for c in calls),
          "exactly one line opens a connection")
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "HttpsTransport":
            inside = [ast.unparse(n.func) for n in ast.walk(node) if isinstance(n, ast.Call)]
            check("http.client.HTTPSConnection" in inside, "and that line is inside the class HttpsTransport")
            check(inside.count("self._key.for_the_request_header_only") == 1
                  and calls.count("self._key.for_the_request_header_only") == 1,
                  "the key is turned back into text in one place only, for the request header")
    writes = [c for c in calls if c in ("os.open", "os.fdopen") or c.endswith((".write_text", ".write_bytes"))]
    plain_open = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and ast.unparse(n.func) == "open"
                  and any(isinstance(a, ast.Constant) and isinstance(a.value, str) and set(a.value) & set("wax+")
                          for a in list(n.args[1:]) + [k.value for k in n.keywords])]
    check(sorted(writes) == ["manifest_path.write_text", "os.fdopen", "os.open"] and not plain_open,
          "files are written in two places only: one attempt file (created new), and the list of names and checksums")
    check("os.O_EXCL" in source and "0o444" in source, "an attempt file is created new and read-only")
    check(not re.search(r"print\(", source.split('_sink = print')[1]),
          "nothing is printed except through the one guarded print function")


def part_start_checks(bench, root):
    case("START CHECKS (rules 1, 2, 3, 6, 11). Everything checked before the first call")
    for run in bench.plan.runs:
        results, _ = capture.start_checks(bench.paths, bench.plan, run, datetime.date(2026, 11, 27), bench.folder())
        check(all(ok for _, ok, _ in results), f"all start checks pass on the constructed repository for {run.id}")
    run = bench.plan.run("anthropic-2026-11-30")
    print("  the real plan against the two real capture documents:")
    for r in bench.plan.runs:
        try:
            capture.check_last_safe_days(capture.Paths(REAL_REPO), r)
            capture.check_prices(capture.Paths(REAL_REPO), r)
            check(True, f"{r.id}: last safe day {r.last_safe_day} and prices equal the documents'")
        except capture.Refused as e:
            check(False, f"{r.id}: {e}")

    def sent(repo):
        return repo / "docs" / "capture" / "sent"

    # rule 2
    v = variant(root, bench.repo, "v-message-changed", lambda r: (sent(r) / "q03.txt").write_bytes(b"CONSTRUCTED changed message"))
    refuses(lambda: capture.check_messages(capture.Paths(v), bench.plan), "rule 2: a message file that differs from its checksum", "q03.txt")
    v = variant(root, bench.repo, "v-final-newline", lambda r: (sent(r) / "q07.txt").write_bytes(message_text(7).encode() + b"\n"))
    refuses(lambda: capture.check_messages(capture.Paths(v), bench.plan), "rule 2: a message file with one line end added", "q07.txt")

    def edit_sums(r):
        text = (sent(r) / "SHA256SUMS").read_text()
        (sent(r) / "q03.txt").write_bytes(b"CONSTRUCTED changed message")
        (sent(r) / "SHA256SUMS").write_text(text.replace(capture.sha256_hex(message_text(3).encode()),
                                                         capture.sha256_hex(b"CONSTRUCTED changed message")))
    v = variant(root, bench.repo, "v-sums-uncommitted", edit_sums, commit=False)
    refuses(lambda: capture.check_messages(capture.Paths(v), bench.plan),
            "rule 2: a message and its checksum both changed, but not committed", "latest commit")
    refuses(lambda: capture.check_tree_is_committed(capture.Paths(v)), "the same change, by the uncommitted-changes check", "not committed")
    v = variant(root, bench.repo, "v-script-edited", lambda r: (r / "capture" / "capture.py").write_text("# CONSTRUCTED edit\n"), commit=False)
    refuses(lambda: capture.check_tree_is_committed(capture.Paths(v)), "a script edited since its commit", "not committed")
    refuses(lambda: capture.check_rehearsal_passed(capture.Paths(v)), "rule 11: a script changed since the rehearsal that passed", "changed since")
    v = variant(root, bench.repo, "v-no-rehearsal", lambda r: (r / "capture" / "rehearsal-result.txt").write_text("REHEARSAL FAILED\n"))
    refuses(lambda: capture.check_rehearsal_passed(capture.Paths(v)), "rule 11: a saved rehearsal result that is not a pass", "does not end with a pass")

    # rule 3
    spending = lambda r: r / "docs" / "spending-record.md"      # noqa: E731
    sums_checksum = capture.sha256_hex((sent(bench.repo) / "SHA256SUMS").read_bytes())
    v = variant(root, bench.repo, "v-no-go", lambda r: spending(r).write_text("# CONSTRUCTED, no go in it\n"))
    refuses(lambda: capture.check_go(capture.Paths(v), run), "rule 3: a spending record with no go for the run", "exactly one go")
    v = variant(root, bench.repo, "v-no-record", lambda r: shutil.move(spending(r), r / "docs" / "moved-away.md"))
    refuses(lambda: capture.check_go(capture.Paths(v), run), "rule 3: no spending record at all", "no docs/spending-record.md")
    v = variant(root, bench.repo, "v-go-lower", lambda r: spending(r).write_text(go_block(run, sums_checksum, ceiling="4.00")))
    refuses(lambda: capture.check_go(capture.Paths(v), run), "rule 3: a go for $4 when the plan's ceiling is $5", "must be equal")
    v = variant(root, bench.repo, "v-go-higher", lambda r: spending(r).write_text(go_block(run, sums_checksum, ceiling="50.00")))
    refuses(lambda: capture.check_go(capture.Paths(v), run), "rule 3: a go for $50 when the plan's ceiling is $5", "must be equal")
    plan_raised = bench.plan_with('ceiling_usd = "5.00"', 'ceiling_usd = "500.00"')
    refuses(lambda: capture.check_go(bench.paths, plan_raised.run(run.id)),
            "rule 3 and 'raise its own ceiling': a plan edited to $500 against a go for $5", "must be equal")
    v = variant(root, bench.repo, "v-go-unquoted", lambda r: spending(r).write_text(
        go_block(run, sums_checksum).replace("> CONSTRUCTED go", "> CONSTRUCTED different words")))
    refuses(lambda: capture.check_go(capture.Paths(v), run), "rule 3: words given as the go that are not quoted in the record", "word for word")
    v = variant(root, bench.repo, "v-go-no-figure", lambda r: spending(r).write_text(
        go_block(run, sums_checksum, words="CONSTRUCTED go with no figure in it")))
    refuses(lambda: capture.check_go(capture.Paths(v), run), "rule 3: quoted words that do not carry the figure", "do not carry")
    v = variant(root, bench.repo, "v-go-old-messages", lambda r: spending(r).write_text(go_block(run, "0" * 64)))
    refuses(lambda: capture.check_go(capture.Paths(v), run), "rule 2: a go that names other message checksums than the repository's", "not the ones")
    v = variant(root, bench.repo, "v-two-goes", lambda r: spending(r).write_text(go_block(run, sums_checksum) * 2))
    refuses(lambda: capture.check_go(capture.Paths(v), run), "rule 3: two goes for one run", "exactly one go")

    # rule 6 and the price list
    later = bench.plan_with('last_safe_day = "2026-11-28"', 'last_safe_day = "2026-11-30"')
    refuses(lambda: capture.check_last_safe_days(bench.paths, later.run(run.id)),
            "rule 6: a plan whose last safe day was moved later than the document's", "what-john-needs-to-do.md says 2026-11-28")
    cheaper = bench.plan_with('price_replied = "15"', 'price_replied = "1.5"')
    refuses(lambda: capture.check_prices(bench.paths, cheaper.run(run.id)), "rule 4: a plan whose price differs from the dated price list", "differ")
    refuses(lambda: capture.check_day(run, datetime.date(2026, 11, 29)), "rule 6: the day after the last safe day", "Nothing is asked")
    capture.check_day(run, datetime.date(2026, 11, 28))
    check(True, "rule 6: the last safe day itself is allowed")

    # rule 1
    case("THE KEY (rule 1). Read from this project's own variable, never printed, never saved")
    os.environ["BTW_CAPTURE_ANTHROPIC_API_KEY"] = CONSTRUCTED_KEY
    os.environ["ANTHROPIC_API_KEY"] = OTHER_PROJECTS_KEY
    key = capture.read_key(run)
    check(key.for_the_request_header_only() == CONSTRUCTED_KEY, "the key comes from BTW_CAPTURE_ANTHROPIC_API_KEY")
    check("BTW_CAPTURE_ANTHROPIC_API_KEY" not in os.environ, "the variable is removed from the environment once read")
    check(key.for_the_request_header_only() != OTHER_PROJECTS_KEY and os.environ.pop("ANTHROPIC_API_KEY") == OTHER_PROJECTS_KEY,
          "a key another project left in ANTHROPIC_API_KEY is not used")
    refuses(lambda: capture.read_key(run), "a run with the variable not set", "is not set")
    check(CONSTRUCTED_KEY not in f"{key} {key!r} {[key]} {key:>5}", "printing the key object shows a fixed phrase, never the key")
    capture._keys_in_use.append(key)
    before = len(SAID)
    capture.say(f"a line that holds {CONSTRUCTED_KEY}")
    check(SAID[before:] == ["[one line withheld: it held the key or words from a reply]"], "a printed line holding the key is withheld")


def part_anthropic(bench):
    run_id = "anthropic-2026-11-30"
    model = bench.plan.run(run_id).models[0]
    name, limit, top = model.name, 32000, model.max_output_tokens

    case("ANTHROPIC, an ordinary run (rules 2, 4, 8, 9; table row 'Any other reply')")
    eng, standin, clock, folder = bench.engine(run_id)
    clean = eng.run_all()
    recs = records(folder)
    check(clean and len(recs) == 50 and len(standin.calls) == 50, "50 exchanges asked, 50 files written, nothing stopped")
    check(all(r["recorded_as"] == capture.REPLY for _, r in recs), "every one recorded as 'a reply'")
    order = [(r["asking_number"], r["question_number"]) for _, r in sorted(recs, key=lambda x: x[1]["asked_at_utc"])]
    check(order == [(a, q) for a in range(1, 6) for q in range(1, 11)], "five rounds, each asking questions 1 to 10 in order")
    check(all(stat.S_IMODE(p.stat().st_mode) == 0o444 for p, _ in recs), "rule 8: every file is read-only")
    check(all(p.name.startswith("CONSTRUCTED__") and r["constructed"] is True and "CONSTRUCTED" in r["what_this_is"]
              and "CONSTRUCTED" in r["reply_text"] for p, r in recs),
          "every stand-in reply is marked constructed in its file name, its record and its own text")
    check(all(re.fullmatch(r"CONSTRUCTED__anthropic__claude-sonnet-4-5-20250929__q\d\d__asking\d__attempt\d\d\.json", p.name)
              for p, _ in recs), "file names carry developer, model, question and asking, and nothing else")
    bodies = [json.loads(req.body) for _, req in standin.calls]
    check(all(set(b) == {"model", "max_tokens", "stream", "messages"} and b["stream"] is True and b["max_tokens"] == limit
              and b["model"] == name and len(b["messages"]) == 1 for b in bodies),
          "rule 9: every request is the streamed Messages request, one message, limit 32000, nothing else in it")
    check(all(req.host == "api.anthropic.com" and req.path == "/v1/messages"
              and dict(req.headers) == {"content-type": "application/json", "anthropic-version": "2026-10-21",
                                        "user-agent": capture.USER_AGENT}
              for _, req in standin.calls), "the address and the fixed headers are the documented ones")
    check(all(r["message_sent"].encode() == bench.messages[f"q{r['question_number']:02d}.txt"]
              and r["message_sha256"] == capture.sha256_hex(bench.messages[f"q{r['question_number']:02d}.txt"])
              for _, r in recs), "rule 2: each record holds the exact message bytes, their file name and checksum")
    wanted = ["message_file", "message_sha256", "message_sent", "request", "service_returned", "reply_text",
              "model_as_reported", "service_id_for_the_reply", "asked_at_utc", "asked_at_pacific",
              "why_the_reply_stopped", "tokens", "reasoning_effort_reported", "cost", "commits"]
    r0 = recs[0][1]
    check(all(k in r0 for k in wanted) and r0["request"]["anthropic_version_header"] == "2026-10-21"
          and "program_library" in r0["request"] and "interface" in r0["request"]
          and "event: message_stop" in r0["service_returned"]["everything_received_in_order"]
          and r0["commits"]["repository_commit"] == bench.commits["repository_commit"],
          "each record holds every item under 'What is saved for each reply', with every stream event received")
    one = (210 * D(3) + 60 * D(15)) / 1000000
    check(all(D(r["cost"]["counted_toward_the_ceiling_usd"]) == one for _, r in recs) and eng.spent() == 50 * one,
          f"rule 4: each reply's cost is worked out from the reported counts, and the running total is their sum ({capture.money(eng.spent())})")
    manifest = (folder.parent / f"{folder.name}-manifest.md").read_text()
    rows = re.findall(r"^([0-9a-f]{64})  (\S+)$", manifest, flags=re.M)
    check(len(rows) == 50 and all(capture.sha256_hex((folder / n).read_bytes()) == c for c, n in rows) and MARK not in manifest,
          "rule 8: the list written at the end holds each file's name and checksum, and no word of any reply")
    check(capture.check_manifest(folder, folder.parent / f"{folder.name}-manifest.md") == [], "the folder matches that list")
    eng2, standin2, _, _ = bench.engine(run_id, folder=folder)
    eng2.run_all()
    check(len(standin2.calls) == 0, "run again on the same folder: nothing is asked twice")
    try:
        eng2.write(recs[0][0].name, {"x": 1}, apart=False)
        check(False, "an existing file cannot be written over")
    except FileExistsError:
        check(True, "an existing file cannot be written over (the attempt raises an error)")

    case("ROW 1. No reply: an error, a timeout, a rate limit. A failed attempt, tried again up to three times, a minute apart")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "http", "status": 529, "error": "overloaded_error"}],
                                                        2: [{"kind": "http", "status": 429, "error": "rate_limit_error"},
                                                            {"kind": "noconnect"},
                                                            {"kind": "http", "status": 500, "error": "api_error"}]})
    eng.run_all()
    check(outcomes(folder, 1) == [capture.FAILED, capture.REPLY], "an overloaded error: kept as a failed attempt, then asked again")
    check(outcomes(folder, 2) == [capture.FAILED] * 3 + [capture.REPLY], "a rate limit, a failed connection and a server error: three failed attempts kept, then a reply")
    check(clock.sleeps == [60, 60, 60, 60], "a minute's wait before each new try")
    check(slot(folder, 1)[0][1]["error_type_reported"] == "overloaded_error" and slot(folder, 1)[0][1]["service_returned"]["http_status"] == 529,
          "the failed attempt's file holds the error as the service gave it")
    check(len(records(folder)) == 54, "every attempt is kept, failed ones included")

    case("ROW 1, continued. Four tries with no reply: left for the next day; after the last safe day, recorded as not made")
    eng, standin, clock, folder = bench.engine(run_id, {3: [{"kind": "http", "status": 500, "error": "api_error"}] * 4})
    clean = eng.run_all()
    check(not clean and outcomes(folder, 3) == [capture.FAILED] * 4 and len(standin.calls) == 6,
          "one try and three more, then the model's run stops for the day; later questions are not asked")
    check(any("left for the next day" in line for line in SAID), "the stop says the question is left for the next day")
    eng, standin, clock2, _ = bench.engine(run_id, folder=folder, clock=Clock(pacific(2026, 11, 28)))
    clean = eng.run_all()
    check(clean and outcomes(folder, 3)[-1] == capture.REPLY and len(standin.calls) == 48,
          "the next day, which is the last safe day, the run carries on from where it stopped and finishes")
    eng, standin, clock, folder = bench.engine(run_id, {3: [{"kind": "http", "status": 500, "error": "api_error"}] * 4})
    eng.run_all()
    eng, standin, _, _ = bench.engine(run_id, folder=folder, clock=Clock(pacific(2026, 11, 29)))
    refuses(lambda: eng.run_all(), "rule 6: carrying on the day after the last safe day", "Nothing is asked")
    check(len(standin.calls) == 0, "and no call was made")
    made = eng.record_not_made()
    not_made = [p for p, r in records(folder) if r["recorded_as"] == capture.NOT_MADE]
    check(made == 48 and len(not_made) == 48 and all(p.name.endswith("__not-made.json") for p in not_made),
          "the 48 askings never completed are each recorded as not made")
    eng_early, _, _, _ = bench.engine(run_id)
    refuses(lambda: eng_early.record_not_made(), "recording askings as not made before the last safe day has passed", "only after")

    case("ROW 2. The reply stopped at the length limit: cut off, kept, asked once more at the model's maximum")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "length"}], 2: [{"kind": "length"}, {"kind": "length"}]})
    eng.run_all()
    check(outcomes(folder, 1) == [capture.CUT_OFF_LENGTH, capture.REPLY] and limits(standin, 1)[:2] == [limit, top],
          f"cut off at {limit}, kept, asked once more at {top}")
    check(outcomes(folder, 2) == [capture.CUT_OFF_LENGTH] * 2 and limits(standin, 2) == [limit, top],
          "cut off again at the maximum: both kept, and it is left; no third asking is made")
    check(any("stopped after the first round" in line for line in SAID[-8:]),
          "and, with three replies of 32,000 tokens or more in round one, rule 5 then stops this run at the $5 ceiling")
    check(clock.sleeps == [], "no wait: a cut-off reply is not a failed attempt")

    case("ROW 3. A streamed reply that ended, after some text, without the signal that it was complete")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "nosignal"}], 2: [{"kind": "nosignal"}, {"kind": "nosignal"}]})
    eng.run_all()
    check(outcomes(folder, 1) == [capture.CUT_OFF_STREAM, capture.REPLY], "recorded as cut off, kept, asked once more")
    check(limits(standin, 1)[:2] == [limit, limit], f"PROPOSED: the second asking is at the same limit ({limit}), not the model's maximum")
    check(outcomes(folder, 2) == [capture.CUT_OFF_STREAM] * 2, "cut off again: both kept, and it is left")
    check(slot(folder, 1)[0][1]["service_signalled_complete"] is False and MARK in slot(folder, 1)[0][1]["reply_text"],
          "the file holds the text that did arrive, and that no completion signal came")

    case("WHICH ROW, WHEN A STREAM BREAKS. Some text arrived: cut off, asked once more, whatever error or timeout came with it")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "error_after_text"}], 2: [{"kind": "timeout_after_text"}]})
    eng.run_all()
    check(outcomes(folder, 1) == [capture.CUT_OFF_STREAM, capture.REPLY], "an error event after some text: cut off, asked once more")
    check(outcomes(folder, 2) == [capture.CUT_OFF_STREAM, capture.REPLY], "a timeout after some text: cut off, asked once more")
    check(clock.sleeps == [], "not treated as a failed attempt: no minute's wait, no three tries")

    case("WHICH ROW, WHEN A STREAM BREAKS. No text arrived: a failed attempt, tried again up to three times, never 'empty'")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "error_before_text"}],
                                                        2: [{"kind": "closed_before_text"}] * 3,
                                                        3: [{"kind": "reasoning_break"}]})
    eng.run_all()
    check(outcomes(folder, 1) == [capture.FAILED, capture.REPLY], "an error event before any text: a failed attempt, tried again")
    check(outcomes(folder, 2) == [capture.FAILED] * 3 + [capture.REPLY], "the connection closing before any text, three times: three failed attempts, then a reply")
    check(outcomes(folder, 3) == [capture.FAILED, capture.REPLY]
          and slot(folder, 3)[0][1]["reasoning_was_sent_before_the_reply"] is True,
          "a break after some reasoning but before any reply text: a failed attempt (reasoning is not reply text)")
    check(capture.EMPTY not in [r["recorded_as"] for _, r in records(folder)], "none of these is recorded as 'empty'")
    worst = eng.most_a_call_could_cost(model, bench.messages["q02.txt"], limit)
    check(D(slot(folder, 2)[0][1]["cost"]["counted_toward_the_ceiling_usd"]) == worst,
          f"rule 4: a broken stream reports no full counts, so the most the call could cost ({capture.money(worst)}) is counted")

    case("THE TWO THINGS THAT COME FIRST. A stream that names a different model and then breaks: the run for that model stops")
    eng, standin, clock, folder = bench.engine(run_id, {2: [{"kind": "wrongmodel_break"}]})
    clean = eng.run_all()
    apart = [p for p, r in records(folder) if r["recorded_as"] == capture.WRONG_MODEL]
    check(not clean and len(standin.calls) == 2 and len(apart) == 1 and apart[0].parent.name == "wrong-model",
          "rule 7: the reply is kept apart in its own folder and no further call is made")
    eng, standin, _, _ = bench.engine(run_id, folder=folder)
    eng.run_all()
    check(len(standin.calls) == 0, "run again: the model's run stays stopped")

    case("THE TWO THINGS THAT COME FIRST. A stream that gives the length limit as its stop reason and then breaks")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "length_break_text"}], 2: [{"kind": "length_break_notext"}]})
    eng.run_all()
    check(outcomes(folder, 1) == [capture.CUT_OFF_LENGTH, capture.REPLY] and limits(standin, 1)[:2] == [limit, top],
          "with some text: the length-limit row governs (cut off, asked once more at the maximum)")
    check(outcomes(folder, 2) == [capture.CUT_OFF_LENGTH, capture.REPLY] and limits(standin, 2)[:2] == [limit, top],
          "with no text: the length-limit row still governs, not the failed-attempt row")

    case("ROW 4. An empty reply whose stop reason is the length limit: cut off, as for a cut-off reply")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "length_empty"}]})
    eng.run_all()
    check(outcomes(folder, 1) == [capture.CUT_OFF_LENGTH, capture.REPLY] and limits(standin, 1)[:2] == [limit, top],
          "recorded as cut off, not as empty, and asked once more at the maximum")

    case("ROW 5. An empty reply for any other reason: empty, kept, asked once more")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "empty"}], 2: [{"kind": "empty"}, {"kind": "empty"}]})
    eng.run_all()
    check(outcomes(folder, 1) == [capture.EMPTY, capture.REPLY] and limits(standin, 1)[:2] == [limit, limit], "empty, kept, asked once more at the same limit")
    check(outcomes(folder, 2) == [capture.EMPTY] * 2, "empty again: both kept, and it is left")

    case("ROW 6. The service blocked the message or the reply: kept, asked once more, never reworded")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "blocked"}]})
    eng.run_all()
    first, second = [req.body for q, req in standin.calls if q == 1][:2]
    check(outcomes(folder, 1) == [capture.BLOCKED, capture.REPLY], "recorded as blocked by the service, kept, asked once more")
    check(first == second, "the second request is byte for byte the first: never reworded")
    check(slot(folder, 1)[0][1]["why_the_reply_stopped"] == "refusal", "the stop reason is saved as the service gave it")

    case("ROW 7. The service reports a different model from the one named: kept apart, the run stops at once")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "wrongmodel"}]})
    clean = eng.run_all()
    check(not clean and len(standin.calls) == 1 and [p.parent.name for p, _ in records(folder)] == ["wrong-model"],
          "rule 7: one call, one file kept apart, nothing more asked")
    check(records(folder)[0][1]["model_as_reported"] == "claude-CONSTRUCTED-other-model", "the name the service reported is saved")

    case("ROW 8. Any other reply: kept, and not asked again, whatever it says")
    eng, standin, clock, folder = bench.engine(run_id, {1: [{"kind": "text", "text": DECLINE}], 2: [{"kind": "text", "text": SHORT}]})
    before = len(SAID)
    eng.run_all()
    check(outcomes(folder, 1) == [capture.REPLY] and len(standin.calls) == 50,
          "a constructed reply that declines is recorded as 'a reply' like any other and is not asked again")
    check(outcomes(folder, 2) == [capture.REPLY], "a constructed three-word reply is kept and is not asked again")
    flagged = [line for line in SAID[before:] if "| very short |" in line]
    check(len(flagged) == 1 and "__q02__asking1__attempt01.json | very short | 3 words (fewer than 20)" in flagged[0],
          "rule 10: the three-word reply is flagged as very short, by name and word count")
    check(not any("__q01__asking1" in line and "|" in line for line in SAID[before:]), "the reply that declines is not flagged: the script never reads what a reply says")


def part_faults(bench):
    case("FAULT FLAGS (rule 10). Empty, very short and ended mid-reply, listed by name, fault and count, never any words")
    roomy = bench.plan_with('ceiling_usd = "5.00"', 'ceiling_usd = "20.00"')     # so that rule 5 does not stop it after round one
    eng, standin, clock, folder = bench.engine("anthropic-2026-11-30", plan=roomy, faults={
        1: [{"kind": "empty"}, {"kind": "empty"}], 2: [{"kind": "text", "text": SHORT}],
        3: [{"kind": "length"}], 4: [{"kind": "nosignal"}], 5: [{"kind": "length_empty"}],
        6: [{"kind": "http", "status": 529, "error": "overloaded_error"}]})
    before = len(SAID)
    eng.run_all()
    said = SAID[before:]
    lines = capture.fault_lines(folder, bench.plan.very_short_words, True)
    kinds = sorted(line.split(" | ")[1] for line in lines)
    check(kinds == ["empty", "empty", "ended mid-reply", "ended mid-reply", "ended mid-reply", "very short"],
          "two empty, one very short, three ended mid-reply (length limit, no completion signal, empty at the length limit)")
    check(not any("__q06__" in line for line in lines), "a failed attempt, which brought no reply, is not listed as a faulty reply")
    form = re.compile(r"CONSTRUCTED__[a-z0-9.\-_]+\.json \| (empty|very short|ended mid-reply) \| [a-z0-9 ,()_]+")
    check(all(form.fullmatch(line) for line in lines), "each line is a file name, the fault, and a count or stop reason, and nothing else")
    check(sum("fault check for round 1: 6 file(s) flagged" in line for line in said) == 1
          and sum("fault check for round 2: 0 file(s) flagged" in line for line in said) == 1,
          "the list is printed after each round")
    check(not any(MARK in line or "not from any model" in line for line in said + lines), "no word of any constructed reply appears in it")
    check(bench.plan.very_short_words == 20, "the threshold is fixed in the plan before the run: 20 words (PROPOSED)")


def part_money(bench):
    run_id = "anthropic-2026-11-30"
    case("THE CEILING (rules 3, 4, 5). The script stops before a call that could pass it")
    tiny = bench.plan_with('ceiling_usd = "5.00"', 'ceiling_usd = "1.00"')
    eng, standin, clock, folder = bench.engine(run_id, plan=tiny)
    clean = eng.run_all()
    check(not clean and len(standin.calls) == 0,
          "ceiling $1: one call at its limit ($0.48) and its one possible repeat at the model's maximum ($0.96) could pass it, so nothing is asked")
    mid = bench.plan_with('ceiling_usd = "5.00"', 'ceiling_usd = "1.50"')
    eng, standin, clock, folder = bench.engine(run_id, plan=mid)
    before = len(SAID)
    clean = eng.run_all()
    check(not clean and 0 < len(standin.calls) < 50 and eng.spent() <= D("1.50"),
          f"ceiling $1.50: {len(standin.calls)} calls made, then stopped with {capture.money(eng.spent())} counted, before the call that could pass it")
    check(any("stopped before a call that could pass the ceiling" in line for line in SAID[before:]), "the stop says why")
    run = bench.plan.run(run_id)
    try:
        run.ceiling_usd = D("500")
        check(False, "refusal 'raise its own ceiling': the ceiling cannot be assigned to")
    except dataclasses.FrozenInstanceError:
        check(True, "refusal 'raise its own ceiling': assigning to the ceiling raises an error")
    try:
        run.last_safe_day = datetime.date(2027, 1, 1)
        check(False, "the last safe day cannot be assigned to")
    except dataclasses.FrozenInstanceError:
        check(True, "assigning to the last safe day raises an error")
    case("RULE 5. After the first round, stop if five rounds at that rate would pass the ceiling")
    eng, standin, clock, folder = bench.engine(run_id, out_tokens=20000)
    before = len(SAID)
    clean = eng.run_all()
    check(not clean and len(standin.calls) == 10 and len(records(folder)) == 10,
          "replies of 20,000 tokens: the first round costs about $3.01, five would cost about $15, over $5; stopped after round one")
    check(any("stopped after the first round" in line for line in SAID[before:]), "the stop says why")
    eng, standin, _, _ = bench.engine(run_id, folder=folder, out_tokens=20000)
    eng.run_all()
    check(len(standin.calls) == 0, "run again: it stops again at the same place without a call")


def part_google(bench):
    run_id = "google-2026-12-01"
    pro, flash = "gemini-2.5-pro", "gemini-2.5-flash"
    case("GOOGLE, the generateContent interface: an ordinary run of both models")
    eng, standin, clock, folder = bench.engine(run_id)
    clean = eng.run_all()
    recs = records(folder)
    check(clean and len(recs) == 100 and all(r["recorded_as"] == capture.REPLY for _, r in recs), "100 exchanges, 100 files, all recorded as 'a reply'")
    bodies = [json.loads(req.body) for _, req in standin.calls]
    check(all(set(b) == {"contents", "generationConfig"} and b["generationConfig"] == {"maxOutputTokens": 32000}
              and len(b["contents"]) == 1 and b["contents"][0]["role"] == "user" for b in bodies),
          "every request holds one user message and the length limit, and nothing else")
    check({req.path for _, req in standin.calls} == {f"/v1beta/models/{pro}:generateContent", f"/v1beta/models/{flash}:generateContent"}
          and all(req.host == "generativelanguage.googleapis.com" and req.key_header == "x-goog-api-key" for _, req in standin.calls),
          "rule 9: the generateContent address for each model, with the key in a header and never in the address")
    r0 = slot(folder, 1, 1, pro)[0][1]
    check(r0["tokens"] == {"sent": 200, "replied_as_billed": 960, "reasoning": 900}
          and D(r0["cost"]["counted_toward_the_ceiling_usd"]) == (200 * D("1.25") + 960 * D("10")) / 1000000,
          "thinking tokens are saved, and charged with the reply at the replied price")
    case("GOOGLE, the failures table")
    eng, standin, clock, folder = bench.engine(run_id, {
        1: [{"kind": "length_empty"}], 2: [{"kind": "blocked"}], 3: [{"kind": "blocked_reply"}], 4: [{"kind": "empty"}],
        5: [{"kind": "http", "status": 429, "error": "RESOURCE_EXHAUSTED"}], 6: [{"kind": "garbled"}],
        7: [{"kind": "wrongmodel"}]})
    eng.run_all()
    check(outcomes(folder, 1, 1, pro) == [capture.CUT_OFF_LENGTH, capture.REPLY] and limits(standin, 1)[:2] == [32000, 65536],
          "row 4: the limit reached while thinking, no text at all: cut off, asked once more at the model's maximum (65536)")
    check(outcomes(folder, 2, 1, pro) == [capture.BLOCKED, capture.REPLY] and slot(folder, 2, 1, pro)[0][1]["why_the_reply_stopped"] == "blockReason:PROHIBITED_CONTENT",
          "row 6: the message blocked by the service: kept, asked once more")
    check(outcomes(folder, 3, 1, pro) == [capture.BLOCKED, capture.REPLY], "row 6: the reply blocked by the service: kept, asked once more")
    check(outcomes(folder, 4, 1, pro) == [capture.EMPTY, capture.REPLY], "row 5: an empty reply: kept, asked once more")
    check(outcomes(folder, 5, 1, pro) == [capture.FAILED, capture.REPLY], "row 1: a rate limit: a failed attempt, tried again")
    check(outcomes(folder, 6, 1, pro) == [capture.FAILED, capture.REPLY], "row 1: a reply that broke off before it could be read: a failed attempt, tried again")
    check(outcomes(folder, 7, 1, pro) == [capture.WRONG_MODEL] and not slot(folder, 8, 1, pro),
          "row 7: a different model reported: kept apart, and the run for gemini-2.5-pro stops at once")
    check(len([1 for _, r in records(folder) if r["model_name_sent"] == flash]) == 50,
          "the run for gemini-2.5-flash, a different model, still goes ahead")
    worst = bench.plan.run(run_id).models[0]
    check(eng.most_a_call_could_cost(worst, b"x", 32000) > D("0.65"),
          "rule 4: until it is checked whether thinking counts inside the limit, a Google call is counted at the model's maximum")


def part_openai(bench):
    run_id, gpt5 = "openai-2026-12-11", "gpt-5-2025-08-07"
    case("OPENAI, the Responses interface: an ordinary run of one model")
    eng, standin, clock, folder = bench.engine(run_id)
    clean = eng.run_all(gpt5)
    recs = records(folder)
    bodies = [json.loads(req.body) for _, req in standin.calls]
    check(clean and len(recs) == 50 and all(r["recorded_as"] == capture.REPLY for _, r in recs), "50 exchanges, 50 files, all recorded as 'a reply'")
    check(all(set(b) == {"model", "input", "max_output_tokens", "store"} and b["store"] is False and b["max_output_tokens"] == 32000 for b in bodies),
          "rule 9: every request sends `store` as false, the length limit, the model and the message, and nothing else")
    check(all(req.host == "api.openai.com" and req.path == "/v1/responses" and req.key_header == "Authorization" for _, req in standin.calls),
          "rule 9: the Responses address")
    r0 = recs[0][1]
    check(r0["tokens"] == {"sent": 200, "replied_as_billed": 700, "reasoning": 640} and r0["reasoning_effort_reported"] == "medium",
          "the count of reasoning tokens, and the reasoning effort the reply reports, are saved")
    case("OPENAI, the failures table")
    eng, standin, clock, folder = bench.engine(run_id, {
        1: [{"kind": "length_empty"}], 2: [{"kind": "blocked"}], 3: [{"kind": "refusal_part", "text": DECLINE}], 4: [{"kind": "empty"}],
        5: [{"kind": "http", "status": 500, "error": "server_error"}], 6: [{"kind": "wrongmodel"}]})
    eng.run_all(gpt5)
    check(outcomes(folder, 1) == [capture.CUT_OFF_LENGTH, capture.REPLY] and limits(standin, 1)[:2] == [32000, 128000],
          "row 4: the limit reached while reasoning, nothing visible: cut off, asked once more at the model's maximum (128000)")
    check(outcomes(folder, 2) == [capture.BLOCKED, capture.REPLY], "row 6: stopped by the service's content filter: kept, asked once more")
    check(outcomes(folder, 3) == [capture.REPLY] and MARK in slot(folder, 3)[0][1]["reply_text"],
          "row 8: words the service files under 'refusal' are kept as a reply and not asked again")
    check(outcomes(folder, 4) == [capture.EMPTY, capture.REPLY], "row 5: an empty reply: kept, asked once more")
    check(outcomes(folder, 5) == [capture.FAILED, capture.REPLY], "row 1: a server error: a failed attempt, tried again")
    check(outcomes(folder, 6) == [capture.WRONG_MODEL] and not slot(folder, 7), "row 7: a different model reported: kept apart, the run stops at once")
    eng, standin, clock, folder = bench.engine("openai-2027-01-14")
    eng.run_all("gpt-4o-2024-08-06")
    check(set(limits(standin, 1)) == {16384}, "the GPT-4o models are sent their own maximum, 16384, which is lower than 32000")


def part_refusals(bench, root):
    plan = bench.plan
    sonnet = plan.run("anthropic-2026-11-30").models[0]
    gemini = plan.run("google-2026-12-01").models[0]
    gpt5 = plan.run("openai-2026-12-11").models[0]
    message = bench.messages["q01.txt"]
    verified = frozenset(capture.sha256_hex(m) for m in bench.messages.values())

    def changed(model, edit, limit=32000, **replace):
        request = capture.build_request(model, message, limit)
        body = json.loads(request.body)
        edit(body)
        request = dataclasses.replace(request, body=json.dumps(body).encode(), **replace)
        return lambda: capture.check_request(request, model, message, limit, verified)

    case("REFUSALS. What a request may never hold; each is refused by the last check before anything is sent")
    capture.check_request(capture.build_request(sonnet, message, 32000), sonnet, message, 32000, verified)
    check(True, "the request the script builds passes that check")
    refuses(changed(sonnet, lambda b: b.update(system="CONSTRUCTED instruction")), "add any instruction: a system message (Anthropic)", "never sent")
    refuses(changed(gpt5, lambda b: b.update(instructions="CONSTRUCTED instruction")), "add any instruction: `instructions` (OpenAI)", "never sent")
    refuses(changed(gemini, lambda b: b.update(systemInstruction={"parts": [{"text": "CONSTRUCTED"}]})), "add any instruction: `systemInstruction` (Google)", "never sent")
    refuses(changed(sonnet, lambda b: b["messages"].append({"role": "user", "content": "CONSTRUCTED second message"})), "add a second message (Anthropic)", "exactly one message")
    refuses(changed(sonnet, lambda b: b["messages"].extend([{"role": "assistant", "content": "CONSTRUCTED"}, {"role": "user", "content": "CONSTRUCTED"}])),
            "send an earlier exchange's text (Anthropic)", "exactly one message")
    refuses(changed(gemini, lambda b: b["contents"].append({"role": "user", "parts": [{"text": "CONSTRUCTED second"}]})), "add a second message (Google)", "exactly one message")
    refuses(changed(gpt5, lambda b: b.update(previous_response_id="resp_CONSTRUCTED")), "send an earlier exchange's id: `previous_response_id` (OpenAI)", "never sent")
    refuses(changed(gemini, lambda b: b.update(previous_interaction_id="CONSTRUCTED")), "send an earlier exchange's id: `previous_interaction_id` (Google)", "never sent")
    refuses(changed(gpt5, lambda b: b.update(conversation="conv_CONSTRUCTED")), "attach the exchange to a stored conversation (OpenAI)", "never sent")
    refuses(changed(sonnet, lambda b: b.update(thinking={"type": "enabled", "budget_tokens": 2000})), "ask for a model's hidden reasoning: `thinking` (Anthropic)", "never sent")
    refuses(changed(gpt5, lambda b: b.update(reasoning={"summary": "auto"})), "ask for a model's hidden reasoning: a reasoning summary (OpenAI)", "never sent")
    refuses(changed(gpt5, lambda b: b.update(include=["reasoning.encrypted_content"])), "ask for a model's hidden reasoning: `include` (OpenAI)", "never sent")
    refuses(changed(gemini, lambda b: b["generationConfig"].update(thinkingConfig={"includeThoughts": True})), "ask for a model's hidden reasoning: `includeThoughts` (Google)", "never sent")
    refuses(changed(sonnet, lambda b: b.update(tools=[{"type": "web_search_20250305", "name": "web_search"}])), "send a tool", "never sent")
    refuses(changed(sonnet, lambda b: b.update(temperature=0)), "send a temperature", "never sent")
    refuses(changed(gpt5, lambda b: b.update(store=True)), "rule 9: OpenAI's `store` sent as true", "store")
    refuses(changed(gpt5, lambda b: b.pop("store")), "rule 9: OpenAI's `store` left out, which the service treats as true", "something other than")
    refuses(changed(sonnet, lambda b: b.update(stream=False)), "rule 9: an Anthropic request that is not streamed", "streamed")
    refuses(changed(sonnet, lambda b: b["messages"][0].update(content=b["messages"][0]["content"] + " Please answer briefly.")),
            "reword: a message that differs from the committed text", "exactly the committed text")
    other = b"CONSTRUCTED message that is not one of the ten"
    refuses(lambda: capture.check_request(capture.build_request(sonnet, other, 32000), sonnet, other, 32000, verified),
            "rule 2: a message that is not one of the ten checked files", "not one of the ten")
    refuses(changed(sonnet, lambda b: None, host="example.invalid"), "a request to any other host", "not the interface")
    refuses(changed(gpt5, lambda b: None, path="/v1/chat/completions"), "rule 9: any other interface of the same service", "not the interface")
    refuses(changed(sonnet, lambda b: None, headers=(("content-type", "application/json"), ("anthropic-beta", "CONSTRUCTED"))), "an extra request header", "never sent")
    refuses(lambda: capture.check_request(capture.build_request(sonnet, message, 64001), sonnet, message, 64001, verified), "a length limit above the model's own maximum", "outside the model")
    refuses(lambda: capture.HttpsTransport(capture.Secret(CONSTRUCTED_KEY)).exchange(
        dataclasses.replace(capture.build_request(sonnet, message, 32000), host="example.invalid")),
        "the network code itself, asked to reach a host that is not one of the three", "not one of the three")

    case("REFUSALS. Where a reply may be written")
    inside = bench.repo / "constructed-replies-inside-a-repository"
    refuses(lambda: bench.engine(folder=inside), "write a reply inside a folder that is part of a git repository", "inside a git repository")
    check(not inside.exists(), "and the folder was not created")
    nested = root / "constructed-nested"
    (nested / ".git").mkdir(parents=True)
    refuses(lambda: bench.engine(folder=nested / "a" / "constructed-b"), "the same, where the repository is two folders up", "inside a git repository")
    real = capture.real_reply_folder(plan)
    existed = real.exists()
    refuses(lambda: bench.engine(folder=real), "a rehearsal writing in the real reply folder", "never writes in the real reply folder")
    refuses(lambda: bench.engine(folder=root / "replies-with-no-mark"), "a rehearsal folder without 'constructed' in its name", "'constructed' in its name")
    refuses(lambda: capture.Engine(plan=plan, run=plan.run("anthropic-2026-11-30"), messages=bench.messages, folder=bench.folder(),
                                   transport=capture.HttpsTransport(capture.Secret(CONSTRUCTED_KEY)), world=Clock(pacific(2026, 11, 27)),
                                   key=capture.Secret(CONSTRUCTED_KEY), mode="rehearsal", commits={}, manifest_path=root / "m.md"),
            "a rehearsal given the real network code", "cannot reach the network")
    refuses(lambda: capture.Engine(plan=plan, run=plan.run("anthropic-2026-11-30"), messages=bench.messages, folder=bench.folder(),
                                   transport=StandIn(), world=Clock(pacific(2026, 11, 27)), key=capture.Secret(CONSTRUCTED_KEY),
                                   mode="real", commits={}, manifest_path=root / "m.md"),
            "a real run given a stand-in in place of the service", "must use the real transport")
    refuses(lambda: capture.Engine(plan=plan, run=plan.run("anthropic-2026-11-30"), messages=bench.messages, folder=bench.folder(),
                                   transport=capture.HttpsTransport(capture.Secret(CONSTRUCTED_KEY)), world=Clock(pacific(2026, 11, 27)),
                                   key=capture.Secret(CONSTRUCTED_KEY), mode="real", commits={}, manifest_path=root / "m.md"),
            "a real run pointed at any folder but the one John ruled", "written only in")
    check(real.exists() == existed, "the real reply folder was not created or touched by any of this")

    case("REFUSALS. Print, summarise or pass on any reply; words from a reply in a file name, a log or the list")
    sealed = capture.Sealed(LONG.format(mark=MARK, n=0))
    check(MARK not in f"{sealed} {sealed!r} {[sealed]} {sealed:>10}" and MARK not in json.dumps({"x": str(sealed)}),
          "a reply turned into text, in any of the usual ways, gives a fixed phrase and never its words")
    before = len(SAID)
    capture.say("a line that carries " + LONG.format(mark=MARK, n=0)[20:90])
    check(SAID[before:] == ["[one line withheld: it held the key or words from a reply]"], "a printed line holding words from a reply is withheld")
    refuses(lambda: capture.no_reply_words("row: " + LONG.format(mark=MARK, n=0), "the list"), "words from a reply in the list of names and checksums", "words from a reply")
    eng, _, _, _ = bench.engine()

    class Wordy:
        developer, name = "anthropic", "constructed reply not from any model"
    refuses(lambda: capture.file_name(Wordy, 1, 1, 1, True), "a file name that is not developer, model, question, asking and attempt", "fixed form")

    case("THE KEY, again. If a service ever sent the key back, it is not saved")
    eng, standin, clock, folder = bench.engine(faults={1: [{"kind": "ok", "headers": [["x-constructed-echo", CONSTRUCTED_KEY]]}]})
    eng.run_all()
    first = slot(folder, 1)[0]
    check(CONSTRUCTED_KEY not in first[0].read_text() and first[1].get("key_was_removed_from_this_record") is True,
          "a constructed reply header that echoes the key: the key is taken out before the file is written, and the file says so")

    case("THE MODE THAT SHOWS A RUN FIRST. It prints what would be sent, to which model, how often and at what cost, and stops")
    before = len(SAID)
    capture.show(bench.paths, plan, plan.run("anthropic-2026-11-30"), datetime.date(2026, 11, 27), False)
    shown = "\n".join(SAID[before:])
    check("Nothing is sent by this command" in shown and "POST https://api.anthropic.com/v1/messages" in shown
          and '"stream": true' in shown and "10 messages x 5 askings = 50" in shown and "estimated cost: $1.5750" in shown
          and "ceiling $5.0000" in shown and "not shown]" in shown and CONSTRUCTED_KEY not in shown,
          "address, headers, the exact body, 50 exchanges, the estimate and the ceiling are shown; the key is not")


def main():
    print("THE REHEARSAL OF THE SEALED CAPTURE SCRIPT")
    print("Every reply below is CONSTRUCTED. No service is called and no model is asked anything.")
    print(f"script: capture/capture.py sha256 {capture.sha256_hex((HERE / 'capture.py').read_bytes())}")
    print(f"plan:   capture/plan.toml  sha256 {capture.sha256_hex((HERE / 'plan.toml').read_bytes())}")
    deliberate = part_tripwire()
    part_source()
    root = pathlib.Path(tempfile.mkdtemp(prefix="btw-capture-rehearsal-constructed-")).resolve()
    print(f"\ntemporary folder for everything written: {root}")
    try:
        check(not capture.inside_a_git_repository(root), "the temporary folder is outside every git repository")
        bench = Bench(root)
        part_start_checks(bench, root)
        part_anthropic(bench)
        part_faults(bench)
        part_money(bench)
        part_google(bench)
        part_openai(bench)
        part_refusals(bench, root)

        case("AT THE END. Across everything above")
        everything = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
        attempt_files = [p for p in everything if p.name.endswith(".json")]
        check(all(p.name.startswith("CONSTRUCTED__") for p in attempt_files),
              f"all {len(attempt_files)} attempt files written are marked constructed in their names")
        check(not any(CONSTRUCTED_KEY in p.read_text(encoding="utf-8", errors="replace") for p in everything),
              f"the constructed key is in none of the {len(everything)} files written")
        check(not any(CONSTRUCTED_KEY in line for line in SAID), f"the constructed key is in none of the {len(SAID)} lines the script printed")
        check(not any(MARK in line or "not from any model" in line for line in SAID), "no word of any constructed reply is in any line the script printed")
        check(not any(MARK in p.name for p in everything), "no word of any constructed reply is in any file name")
        check(capture.withheld_lines == 2, "exactly the two lines withheld on purpose were withheld")
        check(len(TRIPPED) == deliberate, f"the tripwire was touched {len(TRIPPED)} times, all three deliberate: no other code path tried to reach the network")
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print(f"\n{CHECKS} checks, {len(FAILURES)} failed.")
    if FAILURES:
        print("REHEARSAL FAILED:")
        for what in FAILURES:
            print(f"  {what}")
        return 1
    today = datetime.datetime.now(capture.PACIFIC).date()
    print(f"REHEARSAL PASSED {today} capture.py={capture.sha256_hex((HERE / 'capture.py').read_bytes())} "
          f"plan.toml={capture.sha256_hex((HERE / 'plan.toml').read_bytes())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
