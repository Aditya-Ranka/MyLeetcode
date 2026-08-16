#!/usr/bin/env python3
"""
fetcher.py — Pull solved LeetCode problems (code + metadata) for the MyLeetcode sync pipeline.

Auth: uses your logged-in browser session cookie, read from sync/.env
      (LEETCODE_SESSION, LEETCODE_CSRFTOKEN, LEETCODE_USERNAME).

Modes:
  backlog (default)  — paginate ALL your submissions, keep one accepted submission per problem.
  daily              — only accepted submissions newer than --since (unix ts) or last run.

For each problem we keep the latest accepted submission in the most-preferred language the
user actually used for it (default preference: C++, then Python3), so a C++ solution is not
dropped just because the problem was later re-submitted in another language.

Output: sync/submissions.json  (list of problem records; see build_record()).
"""
import argparse
import json
import os
import pathlib
import sys
import time

import requests

HERE = pathlib.Path(__file__).resolve().parent
ENV_PATH = HERE / ".env"
STATE_PATH = HERE / "state.json"
BASE = "https://leetcode.com"
PREFER = ("cpp", "python3", "python", "java", "c")
# Statuses that mean "slow down", not "stop": 429 is the documented rate limit,
# and LeetCode also returns 403 partway through pagination when it throttles an
# IP (hit on the GitHub Actions runner after ~6 pages).
THROTTLE_STATUSES = (403, 429)


def load_env(path=ENV_PATH):
    """Read config from sync/.env if present, then let real environment variables
    override (so GitHub Actions can pass secrets without writing a .env file)."""
    env = {}
    if path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip()
    for k in ("LEETCODE_SESSION", "LEETCODE_CSRFTOKEN", "LEETCODE_USERNAME"):
        if os.environ.get(k):
            env[k] = os.environ[k]
    if not env.get("LEETCODE_SESSION") or not env.get("LEETCODE_CSRFTOKEN"):
        sys.exit("Set LEETCODE_SESSION and LEETCODE_CSRFTOKEN (in sync/.env or as env vars).")
    return env


def make_session(env):
    sess = env.get("LEETCODE_SESSION", "")
    csrf = env.get("LEETCODE_CSRFTOKEN", "")
    if not sess or not csrf:
        sys.exit("LEETCODE_SESSION and LEETCODE_CSRFTOKEN must be set in sync/.env")
    s = requests.Session()
    s.cookies.set("LEETCODE_SESSION", sess, domain="leetcode.com")
    s.cookies.set("csrftoken", csrf, domain="leetcode.com")
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
        "Referer": BASE + "/",
        "Origin": BASE,
        "x-csrftoken": csrf,
        "Content-Type": "application/json",
    })
    return s


def graphql(s, query, variables=None):
    r = s.post(f"{BASE}/graphql", json={"query": query, "variables": variables or {}}, timeout=30)
    r.raise_for_status()
    j = r.json()
    if "errors" in j:
        raise RuntimeError(json.dumps(j["errors"]))
    return j["data"]


def check_auth(s):
    data = graphql(s, "query { userStatus { isSignedIn username } }")
    st = data.get("userStatus") or {}
    if not st.get("isSignedIn"):
        sys.exit("Auth failed: cookie invalid or expired. Refresh LEETCODE_SESSION/csrftoken in sync/.env")
    return st.get("username")


def fetch_submissions_page(s, offset, limit):
    r = s.get(f"{BASE}/api/submissions/", params={"offset": offset, "limit": limit}, timeout=30)
    if r.status_code in THROTTLE_STATUSES:
        return None  # signal caller to back off
    r.raise_for_status()
    return r.json()


def fetch_all_submissions(s, page_size=20, max_pages=500, delay=0.7, stop_before_ts=None,
                          max_attempts=6):
    """Paginate /api/submissions/ (newest first). Optionally stop once we pass stop_before_ts.

    Returns (submissions, complete). `complete` is False when throttling cut the walk
    short, so the caller can refuse to overwrite a good submissions.json with a
    truncated one (pages come newest-first, so a short read drops OLD problems).
    """
    out, offset, pages = [], 0, 0
    while pages < max_pages:
        j = None
        for attempt in range(max_attempts):
            if attempt:  # back off between attempts: 5, 10, 20, 40, 80s
                wait = min(5 * 2 ** (attempt - 1), 120)
                print(f"[fetch] throttled at offset {offset}; retrying in {wait}s "
                      f"(attempt {attempt + 1}/{max_attempts})", file=sys.stderr)
                time.sleep(wait)
            j = fetch_submissions_page(s, offset, page_size)
            if j is not None:
                break
        if j is None:
            print(f"[fetch] still throttled at offset {offset} after {max_attempts} attempts",
                  file=sys.stderr)
            return out, False
        dump = j.get("submissions_dump", [])
        if not dump:
            break
        out.extend(dump)
        pages += 1
        oldest_ts = min(int(x.get("timestamp", 0)) for x in dump)
        if stop_before_ts is not None and oldest_ts <= stop_before_ts:
            break
        if not j.get("has_next"):
            break
        offset += page_size
        time.sleep(delay)
    return out, True


def best_per_problem(subs, since_ts=None, prefer=PREFER):
    """One accepted submission per problem: latest in the most-preferred language present."""
    by_slug = {}
    for sub in subs:
        if sub.get("status_display") != "Accepted":
            continue
        ts = int(sub.get("timestamp", 0))
        if since_ts is not None and ts <= since_ts:
            continue
        by_slug.setdefault(sub.get("title_slug"), []).append(sub)

    best = {}
    for slug, group in by_slug.items():
        chosen = None
        for lang in prefer:
            cands = [x for x in group if x.get("lang") == lang]
            if cands:
                chosen = max(cands, key=lambda x: int(x.get("timestamp", 0)))
                break
        if chosen is None:  # language not in preference list -> latest of whatever exists
            chosen = max(group, key=lambda x: int(x.get("timestamp", 0)))
        best[slug] = chosen
    return best


def get_code(s, sub):
    code = sub.get("code")
    if code:
        return code
    # Fallback: some responses omit code from the list; fetch it explicitly.
    data = graphql(
        s,
        "query d($id: Int!){ submissionDetails(submissionId:$id){ code } }",
        {"id": int(sub["id"])},
    )
    d = data.get("submissionDetails") or {}
    return d.get("code", "")


def get_meta(s, slug):
    data = graphql(
        s,
        """query q($slug: String!){ question(titleSlug:$slug){
              questionFrontendId title titleSlug difficulty topicTags{ name slug } } }""",
        {"slug": slug},
    )
    return data.get("question") or {}


def build_record(s, sub, with_meta=True):
    rec = {
        "slug": sub.get("title_slug"),
        "title": sub.get("title"),
        "lang": sub.get("lang"),
        "timestamp": int(sub.get("timestamp", 0)),
        "submission_id": sub.get("id"),
        "runtime": sub.get("runtime"),
        "memory": sub.get("memory"),
        "code": get_code(s, sub),
    }
    if with_meta:
        m = get_meta(s, rec["slug"])
        rec["frontend_id"] = m.get("questionFrontendId")
        rec["difficulty"] = m.get("difficulty")
        rec["topics"] = [t["name"] for t in (m.get("topicTags") or [])]
        time.sleep(0.4)
    return rec


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", choices=["backlog", "daily"], default="backlog")
    ap.add_argument("--lang", default="", help="restrict to a single language (empty = keep all)")
    ap.add_argument("--since", type=int, default=None,
                    help="daily mode: unix ts; only submissions newer than this")
    ap.add_argument("--out", default=str(HERE / "submissions.json"))
    ap.add_argument("--no-meta", action="store_true", help="skip difficulty/topic lookups")
    ap.add_argument("--max-pages", type=int, default=500)
    args = ap.parse_args()

    env = load_env()
    s = make_session(env)
    user = check_auth(s)
    print(f"[auth] signed in as {user}", file=sys.stderr)

    since = args.since
    if args.mode == "daily" and since is None and STATE_PATH.exists():
        since = json.loads(STATE_PATH.read_text()).get("last_ts")

    subs, complete = fetch_all_submissions(s, max_pages=args.max_pages, stop_before_ts=since)
    print(f"[fetch] {len(subs)} raw submissions", file=sys.stderr)
    if not complete:
        # Overwriting submissions.json with a short read would strip title/difficulty/
        # topics for every problem we never reached, and builder.py regenerates the
        # README from those fields. Leave the last good file alone and try again later.
        sys.exit(f"Throttled before the full history was read — leaving {args.out} "
                 "untouched. Re-run later (or locally, off the datacenter IP).")

    best = best_per_problem(subs, since_ts=since)
    print(f"[dedup] {len(best)} unique accepted problems"
          + (f" since ts={since}" if since else ""), file=sys.stderr)

    results = []
    for slug, sub in sorted(best.items(), key=lambda kv: int(kv[1].get("timestamp", 0))):
        if args.lang and sub.get("lang") != args.lang:
            continue
        rec = build_record(s, sub, with_meta=not args.no_meta)
        results.append(rec)
        print(f"  + #{rec.get('frontend_id','?')} {rec['title']} "
              f"[{rec.get('difficulty','?')}] ({rec['lang']})", file=sys.stderr)

    pathlib.Path(args.out).write_text(json.dumps(results, indent=2))
    if results:
        newest = max(r["timestamp"] for r in results)
        STATE_PATH.write_text(json.dumps({"last_ts": newest, "user": user}, indent=2))
    print(f"[done] wrote {len(results)} problems -> {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
