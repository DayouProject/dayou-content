# AGENTS.md

This repository is `dayou-content`, the Dayou collaboration hub.

It owns:
- onboarding
- workflow documentation
- shared collaboration rules
- the public handoff page at `https://dayouproject.github.io/dayou-content/`

## Shared Dayou Workspace

The full Dayou workspace has three sibling repositories:
- `mysterious`
- `animal-dayou`
- `dayou-content`

When the user asks for `/daily`, `daily`, or `给我一个今天的 /daily`, run the shared Dayou daily workflow below.

Recognized Dayou commands:
- `/route`
- `/context`
- `/issue`
- `/office-hours`
- `/daily`
- `/next`

When the user uses one of these commands in Codex, follow the corresponding behavior below instead of answering loosely.

## Shared `/route` Workflow

1. Check `gh auth status`. If GitHub CLI is unavailable or unauthenticated, stop and tell the user to fix that first.
2. Ensure `mysterious`, `animal-dayou`, and `dayou-content` all exist in the same parent workspace. If a sibling repo is missing, clone it with `gh repo clone DayouProject/<repo>`.
3. Read `README.md`, `TODO.md` when present, and up to 5 open issues from all three repos.
4. If the request is still ambiguous, ask at most 3 short questions.
5. Output exactly:
   - `推荐仓库：`
   - `原因：`
   - `还缺的信息：`
   - `下一步：`
6. If the real next step is `/issue` or `/office-hours`, say so explicitly in `下一步`.

## Shared `/context` Workflow

1. Check `gh auth status`.
2. Ensure the three sibling repos exist locally. Clone missing repos if needed.
3. Choose the focus repo:
   - use the repo named by the user if explicit
   - otherwise use the current repo
4. Read that repo's `README.md`, `TODO.md` when present, and up to 5 open issues.
5. Output exactly:
   - `当前仓库：`
   - `它在做什么：`
   - `已经在推进：`
   - `还没开始：`
   - `现在最值得关注的 3 个点：`
6. Use ordinary Chinese. Do not dump code details.

## Shared `/issue` Workflow

1. Check `gh auth status`.
2. Ensure the three sibling repos exist locally. Clone missing repos if needed.
3. If the target repo is unclear, run the `/route` logic first.
4. Read the target repo's `README.md`, `TODO.md` when present, and up to 5 open issues to avoid obvious duplicates.
5. If key information is missing, ask at most 3 short questions.
6. Output exactly:
   - `Repo：`
   - `Title：`
   - `现状：`
   - `目标结果：`
   - `为什么现在值得做：`
   - `证据 / 链接：`
   - `AI / office hours 判断：`
   - `Done 标准：`
7. Do not invent issue numbers or GitHub state.

## Shared `/office-hours` Workflow

1. Check `gh auth status`.
2. Ensure the three sibling repos exist locally. Clone missing repos if needed.
3. If the target repo is unclear, run the `/route` logic first.
4. Read the target repo's `README.md`, `TODO.md` when present, and up to 5 open issues.
5. If the brief is not ready, ask at most 3 short questions.
6. Output exactly:
   - `背景：`
   - `当前问题：`
   - `现有技术栈：`
   - `最小版本假设：`
   - `约束：`
   - `最想确认的问题：`
   - `会后要带回 GitHub 的结论：`
7. Keep the final questions to 3-5 items. Focus on architecture and version-scope decisions, not vague brainstorming.

## Shared `/daily` Workflow

1. Check `gh auth status`. If GitHub CLI is unavailable or unauthenticated, stop and tell the user to fix that first.
2. Use the parent of the current repo as the Dayou workspace. Ensure `mysterious`, `animal-dayou`, and `dayou-content` all exist there.
3. If any sibling repo is missing, clone it with `gh repo clone DayouProject/<repo>`. Do not silently skip private repo failures; say whether the problem looks like auth, invitation, or repo permission.
4. Read context before writing the daily:
   - `README.md` from all three repos
   - `TODO.md` when present
   - open GitHub issues from all three repos via `gh issue list -R DayouProject/<repo> --state open --limit 5`
5. Default focus repo:
   - use the repo named by the user if explicit
   - otherwise use the current repo
6. If the user did not provide enough context, ask at most 3 short questions first.
7. Output a one-screen Chinese daily with these exact headings:
   - `今天关注的仓库：`
   - `昨天：`
   - `今天：`
   - `Blockers：`
   - `需要确认：`
8. Keep it concrete. Do not invent GitHub state. If data is unavailable, say so explicitly.
9. If the real next step is `/issue` or `/office-hours`, say that in one short line after the daily.

## Shared `/next` Workflow

1. Check `gh auth status`.
2. Ensure the three sibling repos exist locally. Clone missing repos if needed.
3. If the repo or goal is unclear, ask at most 3 short questions.
4. Read the most relevant repo context before answering.
5. Output exactly:
   - `现在先做什么：`
   - `做完后看什么结果：`
   - `如果卡住：`
6. Give the smallest useful next 3 steps, not a long plan.
