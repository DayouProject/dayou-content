# Dayou /next

Follow this workflow exactly.

1. Check `gh auth status`.
2. Use `git rev-parse --show-toplevel` to find the current repo root, then use its parent directory as the Dayou workspace.
3. Ensure the three Dayou repos exist locally. Clone any missing repo with `gh repo clone DayouProject/<repo>`.
4. If the repo or goal is unclear, ask at most 3 short questions.
5. Read the most relevant repo context before answering.
6. Output exactly:

```text
现在先做什么：
做完后看什么结果：
如果卡住：
```

Rules:
- give the smallest useful 3-step path
- prefer concrete actions over abstract advice
- route to `/route`, `/issue`, `/office-hours`, or `/daily` when appropriate
