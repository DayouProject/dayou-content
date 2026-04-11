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
