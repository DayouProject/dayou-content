# Dayou /issue

Follow this workflow exactly.

1. Check `gh auth status`.
2. Use `git rev-parse --show-toplevel` to find the current repo root, then use its parent directory as the Dayou workspace.
3. Ensure the three Dayou repos exist locally. Clone any missing repo with `gh repo clone DayouProject/<repo>`.
4. If the target repo is unclear, run the `/route` logic first.
5. Read the target repo's `README.md`, `TODO.md` when present, and up to 5 open issues to avoid obvious duplicates.
6. If key information is missing, ask at most 3 short questions.
7. Output exactly:

```text
Repo：
Title：
现状：
目标结果：
为什么现在值得做：
证据 / 链接：
AI / office hours 判断：
Done 标准：
```

Rules:
- keep it ready to paste into GitHub
- do not invent issue numbers
- if you saw a likely duplicate, say so briefly in `现状`
