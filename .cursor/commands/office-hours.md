# Dayou /office-hours

Follow this workflow exactly.

1. Check `gh auth status`.
2. Use `git rev-parse --show-toplevel` to find the current repo root, then use its parent directory as the Dayou workspace.
3. Ensure the three Dayou repos exist locally. Clone any missing repo with `gh repo clone DayouProject/<repo>`.
4. If the target repo is unclear, run the `/route` logic first.
5. Read the target repo's `README.md`, `TODO.md` when present, and up to 5 open issues.
6. If the brief is not ready, ask at most 3 short questions.
7. Output exactly:

```text
背景：
当前问题：
现有技术栈：
最小版本假设：
约束：
最想确认的问题：
会后要带回 GitHub 的结论：
```

Rules:
- use ordinary Chinese
- keep `最想确认的问题` to 3-5 items
- focus on scope, architecture, and tradeoffs
- do not turn vague ideas into fake certainty
