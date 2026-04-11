# Dayou /daily

Follow this workflow exactly.

1. Check `gh auth status`. If GitHub CLI is unavailable or unauthenticated, stop and tell the user what to fix first.
2. Use `git rev-parse --show-toplevel` to find the current repo root, then use its parent directory as the Dayou workspace.
3. Ensure these three repos exist in that workspace:
   - `mysterious`
   - `animal-dayou`
   - `dayou-content`
4. If any repo is missing, clone it with:
   - `gh repo clone DayouProject/mysterious`
   - `gh repo clone DayouProject/animal-dayou`
   - `gh repo clone DayouProject/dayou-content`
5. If a private repo fails to clone, do not skip it. Tell the user whether the failure looks like missing invite, missing repo permission, or failed `gh auth`.
6. Read context before writing anything:
   - `README.md` from all three repos
   - `TODO.md` when present
   - open issues from all three repos with `gh issue list -R DayouProject/<repo> --state open --limit 5`
7. Pick the focus repo:
   - use the repo named by the user if explicit
   - otherwise use the current repo
8. If the user did not give enough “昨天 / blockers / today goals” context, ask at most 3 short questions first.
9. Output a one-screen Chinese daily in exactly this format:

```text
今天关注的仓库：
昨天：
今天：
1.
2.
3.

Blockers：
- 

需要确认：
- 
```

Rules:
- keep it short and concrete
- do not invent progress or GitHub state
- if GitHub data is unavailable, say so explicitly
- prefer actions over summaries
- if the right next step is actually `/issue` or `/office-hours`, add one short line after the daily
