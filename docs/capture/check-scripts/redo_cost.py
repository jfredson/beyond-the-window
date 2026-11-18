#!/usr/bin/env python3
"""Redo the arithmetic in docs/capture/cost-and-terms.md from the method's own numbers.

Written 2026-11-17 by the session that wrote docs/capture/check-2026-11-17-second.md (Claude,
Opus 5.5). Prices are as read that day from the developers' pricing pages (addresses in the
report). Calls no service. Also checks the last-safe-day reasoning: when universal midnight
falls in Pacific time on each withdrawal date.
"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

EX = 50                      # ten questions x five askings
SENT = 500                   # tokens sent per exchange, the document's generous figure
PRICES = {  # (sent, replied) dollars per million tokens; replied tokens per exchange
    "claude-sonnet-4-5": (3.00, 15.00, 2000, 32000),
    "gemini-2.5-pro": (1.25, 10.00, 6000, 32000),
    "gemini-2.5-flash": (0.30, 2.50, 6000, 32000),
    "gpt-5": (1.25, 10.00, 6000, 32000),
    "gpt-5-mini": (0.25, 2.00, 6000, 32000),
    "gpt-5-nano": (0.05, 0.40, 6000, 32000),
    "o3": (2.00, 8.00, 6000, 32000),
    "gpt-4o-2024-08-06": (2.50, 10.00, 2000, 16384),
    "gpt-4o-2024-11-20": (2.50, 10.00, 2000, 16384),
    "gpt-4o-mini": (0.15, 0.60, 2000, 16384),
    "gpt-4.1": (2.00, 8.00, 2000, 32000),
    "gpt-4.1-mini": (0.40, 1.60, 2000, 32000),
    "gpt-5-pro": (15.00, 120.00, 15000, 32000),
    "o3-pro": (20.00, 80.00, 15000, 32000),
}
RUNS = {
    "Anthropic, 2026-11-30": (["claude-sonnet-4-5"], 5),
    "Google, 2026-12-01": (["gemini-2.5-pro", "gemini-2.5-flash"], 10),
    "OpenAI, 2026-12-11, no pro": (["gpt-5", "gpt-5-mini", "gpt-5-nano", "o3"], 15),
    "OpenAI, 2027-01-14": (["gpt-4o-2024-08-06", "gpt-4o-2024-11-20", "gpt-4o-mini", "gpt-4.1", "gpt-4.1-mini"], 10),
    "The two pro models": (["gpt-5-pro", "o3-pro"], 200),
}


def cost(m, replied):
    s, r, _, _ = PRICES[m]
    return EX * SENT / 1e6 * s + EX * replied / 1e6 * r


total = total20 = 0
print(f"{'run':30} {'estimate':>9} {'+1/5':>8} {'ceiling':>8} {'all at limit':>13} {'worst one call':>15}")
for run, (models, ceiling) in RUNS.items():
    est = sum(cost(m, PRICES[m][2]) for m in models)
    worst = sum(cost(m, PRICES[m][3]) for m in models)
    one = max(PRICES[m][3] * PRICES[m][1] / 1e6 for m in models)
    print(f"{run:30} {est:9.2f} {est*1.2:8.2f} {ceiling:8.0f} {worst:13.2f} {one:15.2f}")
    if run != "The two pro models":
        total += est
        total20 += est * 1.2
print(f"{'All four (no pro)':30} {total:9.2f} {total20:8.2f} {40:8.0f}")

print()
for d in ["2026-11-30", "2026-12-01", "2026-12-11", "2027-01-14"]:
    u = datetime.fromisoformat(d).replace(tzinfo=timezone.utc)
    p = u.astimezone(ZoneInfo("America/Los_Angeles"))
    print(f"withdrawal {d}: universal midnight is {p:%Y-%m-%d %H:%M} {p.tzname()} Pacific")
