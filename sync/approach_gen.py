#!/usr/bin/env python3
"""
approach_gen.py — fill in approach breakdowns for problems that don't have one yet.

Reads sync/submissions.json, and for every problem whose number is missing from
sync/approaches.json, asks Claude (Anthropic API) to write an approach breakdown
that describes THAT problem's exact submitted code, in the repo's house format.
Uses structured outputs so the reply is always valid JSON.

Env:
  ANTHROPIC_API_KEY   required (get one at console.anthropic.com)
  ANTHROPIC_MODEL     optional, default claude-opus-4-8
                      (claude-sonnet-5 or claude-haiku-4-5 are cheaper)
"""
import json
import os
import pathlib
import sys

from anthropic import Anthropic

HERE = pathlib.Path(__file__).resolve().parent
SUBS = HERE / "submissions.json"
APPR = HERE / "approaches.json"
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-8")

SCHEMA = {
    "type": "object",
    "properties": {
        "approach": {"type": "array", "items": {"type": "string"}},
        "comments": {"type": "array", "items": {"type": "string"}},
        "time": {"type": "string"},
        "space": {"type": "string"},
    },
    "required": ["approach", "time", "space"],
    "additionalProperties": False,
}

PROMPT = """You document LeetCode solutions for a personal study repo. Describe what THIS
specific submitted code does, not a generic textbook solution.

Return:
- approach: 3-6 short bullet strings, each a step of the algorithm AS IMPLEMENTED here.
- comments: 0-2 strings for real gotchas / edge cases / tradeoffs in this code (omit if none).
- time: Big-O time complexity, e.g. "O(n log n)".
- space: Big-O space complexity.

Problem: #{num} {title} [{difficulty}]   topics: {topics}
Language: {lang}

Code:
```
{code}
```"""


def gen_one(client, rec):
    prompt = PROMPT.format(
        num=rec.get("frontend_id"), title=rec.get("title"),
        difficulty=rec.get("difficulty", ""), topics=", ".join(rec.get("topics") or []),
        lang=rec.get("lang"), code=rec.get("code", ""),
    )
    msg = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": SCHEMA}},
        messages=[{"role": "user", "content": prompt}],
    )
    text = next(b.text for b in msg.content if b.type == "text")
    return json.loads(text)


def main():
    subs = json.loads(SUBS.read_text())
    approaches = json.loads(APPR.read_text()) if APPR.exists() else {}
    missing = [r for r in subs if str(r.get("frontend_id")) not in approaches]
    print(f"[approach-gen] {len(missing)} problem(s) need approaches (model={MODEL})", file=sys.stderr)
    if not missing:
        return
    client = Anthropic()  # reads ANTHROPIC_API_KEY from env
    for rec in missing:
        num = str(rec.get("frontend_id"))
        try:
            approaches[num] = gen_one(client, rec)
            print(f"  + #{num} {rec.get('title')}", file=sys.stderr)
        except Exception as e:  # keep going; a bad one shouldn't sink the run
            print(f"  ! #{num} {rec.get('title')}: {e}", file=sys.stderr)
    APPR.write_text(json.dumps(approaches, indent=2, ensure_ascii=False))
    print(f"[approach-gen] approaches.json now has {len(approaches)} entries", file=sys.stderr)


if __name__ == "__main__":
    main()
