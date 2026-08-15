# sync/ — LeetCode → GitHub pipeline

Pulls your accepted LeetCode submissions and files them into this repo's topic
folders, writing an approach breakdown for each in the house format.

## Pieces

| File | Role |
|------|------|
| `fetcher.py` | Pull accepted submissions + code + metadata → `submissions.json` (cache, gitignored). Prefers your latest **C++** solution per problem, else Python. |
| `approach_gen.py` | For any problem missing from `approaches.json`, ask Claude to write the approach breakdown (Anthropic API, structured output). |
| `approaches.json` | Committed knowledge base of approach write-ups, keyed by problem number. |
| `builder.py` | File solutions into Striver-A2Z folders, generate new files, regenerate `README.md`. `--dry-run` to preview. |

## Run it locally

```bash
cp sync/.env.example sync/.env      # then paste your cookie values in
pip install -r sync/requirements.txt
python3 sync/fetcher.py             # -> sync/submissions.json
python3 sync/approach_gen.py        # needs ANTHROPIC_API_KEY in env
python3 sync/builder.py             # writes files + README
```

## The daily cloud job

`.github/workflows/daily-sync.yml` runs the same three steps every day and
commits new solutions automatically. It needs four **repo secrets**
(Settings → Secrets and variables → Actions):

- `LEETCODE_SESSION`, `LEETCODE_CSRFTOKEN`, `LEETCODE_USERNAME`
- `ANTHROPIC_API_KEY`

### Cookie refresh (~monthly)
`LEETCODE_SESSION` expires every 2–4 weeks. When the job fails with
"Auth failed", grab a fresh `LEETCODE_SESSION` / `csrftoken` from
leetcode.com (DevTools → Application → Cookies) and update the two repo secrets.

### Change the run time
Edit the `cron:` line in `daily-sync.yml` (it's in **UTC**). You can also trigger
a run any time from the repo's **Actions** tab → *Daily LeetCode Sync* → *Run workflow*.

### Cost
Approach generation only calls the API for **genuinely new** problems, so quiet
days cost nothing. Default model is `claude-opus-4-8`; set the `ANTHROPIC_MODEL`
env/secret to `claude-sonnet-5` or `claude-haiku-4-5` for cheaper runs.
