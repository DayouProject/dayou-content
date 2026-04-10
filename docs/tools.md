---
title: 工具清单
nav_order: 11
---

# 工具清单

这页只回答两件事：

1. Dayou 协作默认用什么工具
2. 哪些工具是大多数 collaborator 根本不需要碰的

## 默认协作工具

| 工具 | 用途 | 谁需要 |
|------|------|--------|
| **GitHub** | 看进度、开 Issue、留痕、跟进结果 | 所有人 |
| **GitHub Pages** | 看团队手册和协作说明 | 所有人 |
| **一个 AI 入口** | 先把模糊想法整理清楚，再继续带你走流程 | 所有人 |
| **gstack office hours** | 做专项技术 sanity check | 需要时使用 |
| **微信** | 处理紧急问题和权限问题 | 所有人 |

## AI 工具怎么选

Dayou 不要求大家一开始就统一到同一个 AI 客户端。

默认原则是：

- 先保证你至少有一个能工作的 AI 入口
- 再让它读 Dayou 的 AI 接管入口页
- 再让它继续帮你做 repo 路由、Issue 草稿、office hours 准备和 `/daily`

| AI 路线 | 适合谁 | 默认建议 |
|---|---|---|
| **ChatGPT / Claude 网页版** | 大多数 collaborator | 最推荐，浏览器即可 |
| **Cursor** | 已经习惯编辑器的人 | 可选增强，不是默认门槛 |
| **Codex / Claude Code** | 更偏技术的协作者 | 可用，但不适合新人默认路线 |
| **gstack office hours** | 需要技术方向判断时 | 专项使用，不是日常入口 |

如果你还没配好，先看 [AI 配置](./ai-setup)。

如果你已经配好，下一步直接看 [AI 接管入口](./ai-handoff)。

## 产品与系统工具

这些工具真实存在，但不是每个人都要碰：

| 工具 | 用途 | 默认由谁处理 |
|------|------|-------------|
| **Vercel** | 产品部署 | Lexa |
| **Upstash Redis** | 数据存储 | Lexa |
| **Stripe** | 支付 | Lexa |
| **OpenAI / Gemini API** | AI 相关能力 | Lexa |
| **HeyGen** | 视频生成 | Lexa |
| **n8n** | 自动化工作流 | Lexa |

## 默认你需要装什么

对大多数不会写代码的 collaborator：

- 必需：浏览器
- 必需：GitHub 账号
- 必需：一个 AI 入口
- 推荐：把 [AI 接管入口](./ai-handoff) 收藏起来
- 可选：GitHub 手机 App
- 可选：微信

## 默认你不需要装什么

- `git`
- GitHub Desktop
- VS Code
- Node.js / npm
- 一上来就装 Codex CLI
- 一上来就装 Claude Code
- Vercel CLI
- 任何本地开发环境

如果以后你真的需要更重的工具，那是例外，不是默认。

## 我什么时候该用什么

| 你现在要做什么 | 默认用什么 |
|------|------|
| 看项目现在在做什么 | GitHub 仓库里的 `README`、`TODO`、open Issues |
| 判断一个想法值不值得提 | 先问 AI |
| 判断该不该去 gstack office hours | 先让 AI 帮你整理问题，再决定 |
| 生成 daily | 让 AI 走 `/daily` |
| 正式提需求 | GitHub Issue |
| 跟进结果 | 回到原 Issue |
| 当天必须处理的异常 | 微信提醒，然后补回 Issue |

## 移动端能不能协作

可以。

- 看文档：手机浏览器即可
- 看 Issues：手机浏览器或 GitHub App 都可以
- 提需求：仍然建议用 GitHub 网页里的 Issue 模板

## 工具相关的真实边界

- 你可以参与项目，不等于你必须会本地开发
- 你可以先问 AI，不等于正式决定可以只停留在聊天记录里
- 你可以用手机协作，不等于 Issue 可以省略
- 你可以选不同的 AI 客户端，不等于 Dayou 的协作规则可以不统一

## 相关页面

- [AI 配置](./ai-setup)
- [AI 接管入口](./ai-handoff)
- [组织级 AI Skills](./organization-skills)
- [仓库分工](./repo-scope)
- [每周工作流](./workflow)
- [GitHub 零基础入门](./github-beginner-guide)
