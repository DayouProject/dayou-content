---
name: daily
description: Generate a one-screen Chinese daily operations report for the Dayou content team by reading team.yaml, the current weekly manifest, GitHub issues, and content pipeline artifacts.
---

# /daily

为 Dayou 内容运营团队生成一屏内中文日报。优先读取 `team.yaml`、`config.yaml`、`workspace/scripts/*/manifest.json`、GitHub Issues，以及可用时的 GitHub Project `Dayou Content Pipeline`。

## Role Detection

1. 先读取 `team.yaml`。
2. 如果当前用户是 `AlyciaBHZ`，或显式提到 founder / Lexa，使用 `founder` 模式。
3. 如果当前用户在 `team.yaml` 中的 `role` 是 `content_lead`，使用 `content_lead` 模式。
4. 如果当前用户在 `team.yaml` 中的 `role` 是 `content_reviewer`，使用 `content_reviewer` 模式。
5. 如果无法判断，默认使用 `founder` 模式，但开头注明“角色未识别，按 founder 视角汇总”。

## Workflow

1. 读取 `config.yaml`，确认 `workspace` 根目录、发布时区、每周脚本目标数。
2. 在 `workspace/scripts/` 下找到最新周目录，读取对应 `manifest.json`。
3. 统计流水线状态：
   - `已生成`：manifest 中 `scripts` 总数。
   - `已审核`：优先读显式审核字段，如 `review.status`、`status`、`approved_by`；若没有，则检查脚本 markdown 中是否出现 `approved`、`审核通过`、`ready to publish` 等标记。
   - `已发布`：任一平台 publish 状态为 `published`、`posted`、`scheduled`、`success` 记为进入发布队列；真正已发布优先看 `published` / `posted`。
   - `视频完成`：`video.status` 非 `dry_run` 且存在 `video_url` 或 `video_id`。
4. 输出未来 3 天排期：
   - 从 manifest 的 `scheduled_for` 排序。
   - 只列最近 3 天内的内容，包含日期、标题、平台状态。
5. 如果存在 GitHub Project `Dayou Content Pipeline`，读取当前卡片并按 `Pipeline Stage` 或默认状态字段分组，找出堵点阶段。
6. 如果 GitHub 可用，扫描 open issues：
   - `label:content-idea state:open`
   - `label:weekly-report state:open`
7. 查找最新一条 `weekly-report` issue，提取：
   - 本周发布数
   - Views / Likes / Comments / Shares
   - Top Performer
   - Audience Feedback
   - 下周方向
8. 从 issue 作者、assignee、评论者、project 卡片责任人中识别团队活动：
   - 谁提交了内容想法
   - 谁做了 review
   - 哪些环节无人认领
9. 给出“决策项”和“下一步动作”时，只写最影响本周发布节奏的 2-3 条。

## Founder Mode

除通用部分外，额外包含：

- GitHub Issues 扫描：打开的 `content-idea` 与 `weekly-report`
- 社媒账号状态检查：对照 `team.yaml > social_accounts`
- 内容表现摘要：最新周报中的核心指标、最佳内容、异常项
- 团队活动：谁提交 ideas、谁 review、谁推进 publish
- 决策需求：例如账号未开通、选题不足、审核堆积、视频环节卡住
- 建议动作：按“今天必须做 / 本周应做”排序

## Content Lead Mode

除通用部分外，额外包含：

- 我的待审脚本：manifest 或脚本文件中状态未完成、且需要 review 的条目
- 我提交的 ideas：我创建的 `content-idea` issue 当前状态
- 本周发布日历：本周剩余内容按日期列出
- 建议选题：从 `corpus/` 中找尚未被本周 manifest `source_path` 使用的来源，优先推荐能转成 TikTok 钩子的题目

## Content Reviewer Mode

除通用部分外，额外包含：

- 待我审核：脚本草稿中最接近发布时间但仍未通过的条目
- 风险提醒：是否有容易触发误导、过度承诺、宗教敏感或平台审核风险的表达
- 今日 review 顺序：只列 3 条，按发布时间最近优先

## Output Rules

- 全部使用中文。
- 控制在一屏内，优先短句、半结构化输出。
- 每个区块最多 2-3 行，不要写成长段落。
- 如果 GitHub / Project 数据不可用，明确写“GitHub 未连接”或“Project 未配置”，不要假装有数据。
- 不重复 manifest 里的完整文案，只输出运营决策所需摘要。

## Output Template

按下面格式输出，保持精简：

```text
Dayou 日报 | 角色: founder | 周: 2026-W16

流水线
- 已生成 7/7，已审核 0，视频完成 0，已发布 0
- 卡点：Review 空缺，TikTok 账号仍待 setup

未来 3 天
- 04-13: What to do when life feels uncertain | TikTok dry_run
- 04-14: How to stop forcing timing | TikTok dry_run
- 04-15: Why ambition needs inner steadiness | TikTok dry_run

GitHub
- Content ideas: 2 个 open，最新由 XXX 提交
- Weekly report: 1 个 open，最新周报显示本周发布 3/7

表现
- 最佳内容：XXX，Views 12.4k
- 异常：评论高但分享低，说明话题有讨论性但传播力不足

团队
- 提案：XXX
- 审核：暂无明确 owner

决策项
- 是否先完成 TikTok 正式账号开通，再推进批量发布
- 是否补 2 个非《易经》选题，避免题材过窄

下一步
- 今天：补齐 review owner，并确认 04-13 首发稿
- 本周：建立 Project 看板并开始记录 stage 流转
```
