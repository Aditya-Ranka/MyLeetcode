#!/usr/bin/env python3
"""
approach_gen.py — fill approach breakdowns for new problems using any
OpenAI-compatible LLM API (Groq, Google Gemini, Cerebras, OpenAI, OpenRouter, ...).

Reads sync/submissions.json; for every problem missing from sync/approaches.json,
asks the model to describe THAT problem's exact submitted code in the house format,
and writes the result back. Only new problems cost an API call.

Env:
  LLM_API_KEY    required   — your provider API key
  LLM_BASE_URL   optional   — default https://api.groq.com/openai/v1   (Groq)
                              Gemini:  https://generativelanguage.googleapis.com/v1beta/openai/
                              Cerebras: https://api.cerebras.ai/v1
  LLM_MODEL      optional   — default "llama-3.3-70b-versatile" (Groq).
                              VERIFY the current id in your provider's model list
                              (Gemini e.g. "gemini-2.5-flash").
"""
import json
import os
import pathlib
import re
import sys

from openai import OpenAI

HERE = pathlib.Path(__file__).resolve().parent
SUBS = HERE / "submissions.json"
APPR = HERE / "approaches.json"
BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.groq.com/openai/v1")
MODEL = os.environ.get("LLM_MODEL", "llama-3.3-70b-versatile")

PROMPT = """You document LeetCode solutions for a personal study repo. Describe what THIS
specific submitted code does, not a generic textbook solution.

Respond with ONLY a JSON object (no markdown fences) with these keys:
- "approach": array of 3-6 short strings, each a step of the algorithm AS IMPLEMENTED here.
- "comments": array of 0-2 strings for real gotchas/edge cases/tradeoffs in this code (use [] if none).
- "time":  string, Big-O time complexity, e.g. "O(n log n)".
- "space": string, Big-O space complexity.

Problem: #{num} {title} [{difficulty}]   topics: {topics}
Language: {lang}

Code:
```
{code}
```"""


def extract_json(text):
    """Parse the model's reply into a dict, tolerating stray prose or ``` fences."""
    text = (text or "").strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.S)
        if not m:
            raise
        return json.loads(m.group(0))


def normalize(d):
    ordered = {"approach": [str(x) for x in (d.get("approach") or [])]}
    if d.get("comments"):
        ordered["comments"] = [str(x) for x in d["comments"]]
    ordered["time"] = str(d.get("time", ""))
    ordered["space"] = str(d.get("space", ""))
    return ordered


def gen_one(client, rec):
    prompt = PROMPT.format(
        num=rec.get("frontend_id"), title=rec.get("title"),
        difficulty=rec.get("difficulty", ""), topics=", ".join(rec.get("topics") or []),
        lang=rec.get("lang"), code=rec.get("code", ""),
    )
    kwargs = dict(model=MODEL, temperature=0.2,
                  messages=[{"role": "user", "content": prompt}])
    try:  # JSON mode where supported; fall back to plain if the model rejects it
        resp = client.chat.completions.create(response_format={"type": "json_object"}, **kwargs)
    except Exception:
        resp = client.chat.completions.create(**kwargs)
    return normalize(extract_json(resp.choices[0].message.content))


def main():
    if not os.environ.get("LLM_API_KEY"):
        sys.exit("LLM_API_KEY is not set (your Groq/Gemini/etc. key).")
    subs = json.loads(SUBS.read_text())
    approaches = json.loads(APPR.read_text()) if APPR.exists() else {}
    missing = [r for r in subs if str(r.get("frontend_id")) not in approaches]
    print(f"[approach-gen] {len(missing)} problem(s) need approaches "
          f"(model={MODEL} @ {BASE_URL})", file=sys.stderr)
    if not missing:
        return
    client = OpenAI(base_url=BASE_URL, api_key=os.environ["LLM_API_KEY"])
    for rec in missing:
        num = str(rec.get("frontend_id"))
        try:
            approaches[num] = gen_one(client, rec)
            print(f"  + #{num} {rec.get('title')}", file=sys.stderr)
        except Exception as e:  # one bad problem shouldn't sink the run; retried next time
            print(f"  ! #{num} {rec.get('title')}: {e}", file=sys.stderr)
    APPR.write_text(json.dumps(approaches, indent=2, ensure_ascii=False))
    print(f"[approach-gen] approaches.json now has {len(approaches)} entries", file=sys.stderr)


if __name__ == "__main__":
    main()
