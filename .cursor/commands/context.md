# Dayou /context

Follow this workflow exactly.

1. Check `gh auth status`.
2. Use `git rev-parse --show-toplevel` to find the current repo root, then use its parent directory as the Dayou workspace.
3. Ensure the three Dayou repos exist locally. Clone any missing repo with `gh repo clone DayouProject/<repo>`.
4. Pick the focus repo:
   - use the repo named by the user if explicit
   - otherwise use the current repo
5. Read that repo's `README.md`, `TODO.md` when present, and up to 5 open issues.
6. Output exactly:

```text
当前仓库：
它在做什么：
已经在推进：
还没开始：
现在最值得关注的 3 个点：
```

Rules:
- explain in ordinary Chinese
- do not dump code internals
- if TODO or issues are missing, say so explicitly
