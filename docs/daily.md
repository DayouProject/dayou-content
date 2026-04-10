---
title: /daily 模板
nav_order: 9
---

# /daily 模板

这页是 Dayou 的 `/daily` 专用输出模板页。

目标不是写漂亮日报，而是让 AI 用最短格式帮你回答：

- 今天应该关注哪个仓库
- 今天最重要的 3 件事是什么
- 当前卡点是什么
- 需要谁确认什么

## 什么时候该用 `/daily`

适合这些情况：

- 你想快速对齐今天要推进什么
- 你刚看完 README / TODO / open Issues，想让 AI 压缩重点
- 你手头事情很多，想让 AI 帮你做优先级
- 你想给团队一个短而清楚的 daily

## `/daily` 的标准输出格式

```text
今天关注的仓库：

昨天：
- 

今天：
1.
2.
3.

Blockers：
- 

需要确认：
- 
```

## 复制即用的 AI 指令

```text
请基于我给你的 Dayou 上下文，生成今天的 /daily。

要求：
1. 用普通中文
2. 只保留最重要的内容
3. 如果信息不足，先问我最多 3 个问题
4. 输出格式必须是：

今天关注的仓库：
昨天：
今天：
Blockers：
需要确认：
```

## 你至少要喂给 AI 什么

| 输入 | 最低要求 |
|---|---|
| 当前仓库 | 至少说清是 `mysterious`、`animal-dayou` 还是 `dayou-content` |
| 当前上下文 | README、TODO、open Issues，或者你自己的简述 |
| 昨天做了什么 | 没有也可以留空，让 AI 帮你用“当前状态”替代 |
| 当前卡点 | 有没有权限、信息不全、技术路径不确定等 |
| 今天目标 | 今天最想推进的方向 |

## 模拟用例 1

下面是**模拟用例**，不代表当前仓库真实状态。

### 原始输入

```text
请给我一个 dayou-content 的 /daily。

背景：
- 我们刚把 GitHub Pages 站点统一成 Dayou 协作门户
- 现在重点是补 AI onboarding
- 我昨天已经把 AI 配置、AI 接管入口、组织级 AI skills 写出来了
- 今天还缺 gstack office hours 模板和 /daily 模板
- 当前 blockers：需要确认模板到底该写到什么颗粒度
```

### 输出示例

```text
今天关注的仓库：
dayou-content

昨天：
- 已补齐 AI 配置页
- 已补齐 AI 接管入口页
- 已定义组织级 AI skills

今天：
1. 补 gstack office hours 专用模板页
2. 补 /daily 专用输出模板页
3. 把这两页从首页和 AI 接管入口挂出来，形成完整入口链路

Blockers：
- 需要确认模板是偏“复制即用”，还是偏“规则说明”

需要确认：
- 这两页是否要附带模拟用例
- 首页是否要把它们提升到第一屏入口
```

## 模拟用例 2

这也是**模拟用例**，用于展示另一种更偏产品仓库的 daily。

### 原始输入

```text
请给我一个 mysterious 的 /daily。

背景：
- 有一个需求是想降低 collaborator 提需求的门槛
- 用户现在可能先通过 dayou-content 读规则，再进入主产品仓库开 Issue
- 昨天主要在确认跨仓库协作口径
- 今天想判断主产品这边最适合先接什么能力
- 当前 blocker：还没有把主产品侧的 intake 需求切成第一版 Issue
```

### 输出示例

```text
今天关注的仓库：
mysterious

昨天：
- 已对齐跨仓库协作口径
- 已把非技术 collaborator 的默认路径转到 AI → Issue

今天：
1. 判断主产品侧第一版 intake 需求应该落在哪个 Issue
2. 明确哪些能力属于主产品，哪些应该继续留在 dayou-content
3. 把第一版 done 标准写清楚，避免需求继续漂移

Blockers：
- intake 需求的第一版边界还不够明确

需要确认：
- 第一版是否只做 Issue 草稿生成
- 是否需要马上进入自动化实现
```

## 一个好的 `/daily` 应该长什么样

它应该：

- 短
- 明确
- 可执行
- 一眼能看出今天先做什么

它不应该：

- 变成长周报
- 把所有背景重写一遍
- 只有抽象方向，没有动作

## 如果你想让 AI 先判断再写 `/daily`

先发这句：

```text
如果信息不够，不要直接瞎写 /daily。先问我最多 3 个问题，再输出最终版本。
```

## 相关页面

- [AI 接管入口](./ai-handoff)
- [组织级 AI Skills](./organization-skills)
- [gstack Office Hours](./gstack-office-hours)
