---
title: AI 配置
nav_order: 5
---

# AI 配置

这页只回答三件事：

1. 你到底该选哪个 AI 入口
2. 什么叫“已经配置完成”
3. 配完以后，下一步该把哪个链接贴给 AI

## 先讲结论

Dayou 现在不要求每个人都装同一款 AI 工具。

第一目标不是“全员都会用 Codex / Claude Code / Cursor”，而是：

- 每个人至少有一个能工作的 AI 入口
- 这个 AI 能读 Dayou 的协作说明
- 这个 AI 能继续带你走后面的流程

对大多数 collaborator，推荐顺序是：

1. ChatGPT 或 Claude 网页版
2. Cursor
3. Codex / Claude Code
4. gstack office hours 作为专项技术咨询，不是日常入口

## 你该选哪条路

| 你的情况 | 推荐选择 | 原因 |
|---|---|---|
| 完全不会代码，只想先参与协作 | ChatGPT 或 Claude 网页版 | 浏览器即可，最轻，最容易上手 |
| 已经在用编辑器，想把 AI 放在一个熟悉的地方 | Cursor | 适合已经有编辑器习惯的人 |
| 已经能用终端或本地工具 | Codex / Claude Code | 更强，但不适合作为新人默认路线 |
| 想确认技术栈是否合理、想问系统级问题 | gstack office hours | 适合专项技术判断，不适合日常陪跑 |

## 不要先统一客户端，先统一目标

不同 AI 的具体按钮和界面会变，但 Dayou 真正关心的是这四个结果：

1. 你能开一个新的干净对话
2. 你能把链接或文字喂给 AI
3. AI 能用普通中文回答你
4. AI 能帮你产出 `repo 路由 / office hours 准备 / daily / Issue 草稿`

如果这四件事都做到了，就算配置完成。

## 配置完成的标准

你的 AI 满足下面这张表，就可以进入 Dayou 工作流：

| 检查项 | 通过标准 |
|---|---|
| 账号可用 | 你能正常登录，不会频繁被卡在权限或订阅问题 |
| 能开新对话 | 你能针对不同主题单独开新 chat |
| 能读链接或读粘贴文本 | 你能把 Dayou 页面链接或页面内容喂给 AI |
| 能输出中文结构化结果 | 它能给你 repo 判断、Issue 草稿、daily 草稿 |
| 能连续跟进同一话题 | 它不会第一轮说清楚，第二轮就完全忘掉目标 |

## 四条 AI 路线怎么理解

### 1. ChatGPT / Claude 网页版

这是 Dayou 当前最推荐的大众路线。

适合：

- 非技术 collaborator
- 只想通过浏览器参与的人
- 先想跑通“AI 带我协作”这条线的人

你只需要确保：

- 能登录
- 能开新 chat
- 能粘贴链接
- 能让它先读链接，再继续对话

### 2. Cursor

如果你已经习惯在 Cursor 里工作，可以继续用它。

但 Dayou 不要求你一开始就 clone 仓库或本地跑项目。

第一阶段你只需要让 Cursor 里的 AI：

- 读 Dayou 的 AI 接管入口页
- 帮你判断事情属于哪个仓库
- 帮你整理 office hours 问题
- 帮你写 GitHub Issue 草稿

### 3. Codex / Claude Code

这是更偏技术协作者的路线。

如果你已经会用，可以继续用；如果你不会，不要把它当成 Dayou 默认起点。

对新人来说，先把“浏览器协作 + AI 路由 + Issue 留痕”跑通，更重要。

### 4. gstack office hours

这不是日常 AI 入口，而是专项技术判断入口。

什么时候该用它：

- 你不确定现有技术栈能不能做
- 你想确认自动化或系统设计是否合理
- 你需要更高层的技术 sanity check

什么时候不该先上来就用它：

- 你还没把问题整理清楚
- 你还没判断属于哪个仓库
- 你只是想把模糊想法先变成清楚问题

## 你配好 AI 之后，第一件事做什么

把这页链接贴给 AI：

`https://dayouproject.github.io/dayou-content/ai-handoff.html`

然后发这段话：

```text
请先阅读这个 Dayou 页面，然后作为我的协作 AI 继续带我走流程：
https://dayouproject.github.io/dayou-content/ai-handoff.html

先用普通中文总结 Dayou 三个仓库的区别，再问我最多 3 个问题，判断我现在更需要：
1. repo 路由
2. gstack office hours 准备
3. /daily
4. GitHub Issue 草稿

默认把我当成不会写代码的 collaborator，不要一上来让我装本地开发工具。
```

## 第一次测试，AI 应该做到什么

第一次测试通过，通常会看到这些结果：

- 它先解释 `mysterious / animal-dayou / dayou-content`
- 它不会假定你是什么固定岗位
- 它会问你问题属于哪个产品、现状是什么、想要什么结果
- 如果你方向还模糊，它会先帮你整理
- 如果技术可行性不确定，它会把你引到 `office hours brief`
- 如果需求已经成形，它会给你一份 GitHub Issue 草稿

## 如果 AI 读不了链接怎么办

不要卡住，直接换成下面的兜底方式：

1. 打开 [AI 接管入口](./ai-handoff)
2. 把页面内容整段复制进 AI
3. 再让它继续带你走流程

## 相关页面

- [AI 接管入口](./ai-handoff)
- [gstack Office Hours](./gstack-office-hours)
- [/daily 模板](./daily)
- [组织级 AI Skills](./organization-skills)
- [工具清单](./tools)
- [GitHub 零基础入门](./github-beginner-guide)
