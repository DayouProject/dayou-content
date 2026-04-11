# Dayou /route

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
5. Read `README.md`, `TODO.md` when present, and up to 5 open issues from all three repos.
6. If the request is still ambiguous, ask at most 3 short questions.
7. Output exactly:

```text
推荐仓库：
原因：
还缺的信息：
下一步：
```

Rules:
- use ordinary Chinese
- make one clear recommendation
- if the real next step is `/issue` or `/office-hours`, say that in `下一步`
- do not invent GitHub state
