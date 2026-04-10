---
title: 工具清单
nav_order: 7
---

# 工具清单

我们用什么工具，谁负责，账号在哪。

## 协作工具（所有人用）

| 工具 | 用途 | 谁主要用 | 链接 |
|------|------|----------|------|
| **GitHub** | 内容协作、Issue、文档 | 所有人 | [仓库](https://github.com/AlyciaBHZ/dayou-content) |
| **GitHub Pages** | 团队手册（你正在看的） | 所有人 | [手册站点](https://alyciabhz.github.io/dayou-content/) |
| **微信** | 紧急同步、登不上账号 | 所有人 | 私聊 Lexa |

## 内容生产工具（Lexa 主管）

| 工具 | 用途 | 状态 | 链接 |
|------|------|------|------|
| **OpenAI / Gemini API** | AI 脚本生成 | 已配置 | API key 在 .env |
| **HeyGen** | AI Avatar 视频生成 | 待开通 | https://heygen.com |
| **n8n** | 自动发布工作流 | 待配置 | 自部署或 cloud |
| **Vercel** | dayou.dev 产品部署 | 已上线 | https://dayou.dev |
| **Upstash Redis** | 数据存储 | 已上线 | mysterious 项目用 |

## 社媒账号（宣发负责人主管）

| 平台 | 账号 | 状态 | 用途 |
|------|------|------|------|
| **TikTok** | `@dayou.wisdom` | 待开通 | 主要发布渠道 |
| **Instagram** | `@dayou.wisdom` | 待开通 | 跨平台同步 |
| **Reddit** | r/taoism + r/astrology | 待启动 | 社区种草 |
| **X (Chinese)** | TBD | 已有，流量低 | 备用 |
| **X (English)** | TBD | 已有，流量低 | 备用 |

{: .note }
> 账号开通后，把账号链接和登录信息（不要密码）记录到 `team.yaml` 的 `social_accounts` 段。

## 知识库工具（知识库负责人主管）

| 工具 | 用途 | 状态 |
|------|------|------|
| **GitHub Issues** | 提交内容概念 | 已上线 |
| **CULTURAL_TRANSLATION.md** | 海外术语翻译规则 | 已上线 |
| **大师私有知识库** | 经典出处、解读框架 | 大师持有 |

## 数据与监控工具

| 工具 | 用途 | 谁看 |
|------|------|------|
| **TikTok Creator 后台** | 视频数据 | 宣发负责人 |
| **Instagram Insights** | 视频数据 | 宣发负责人 |
| **Vercel Analytics** | dayou.dev 流量 | Lexa |
| **Stripe Dashboard** | 海外支付 | Lexa |
| **GitHub Issues `weekly-report` label** | 周报汇总 | 所有人 |

## 我应该装什么

### 知识库负责人

- **必装**：浏览器（Chrome/Edge/Safari）
- **建议装**：GitHub 手机 App（可选，方便手机看 Issue）
- **不需要装**：任何代码编辑器、Git、Python

### 宣发负责人

- **必装**：浏览器、TikTok App、Instagram App
- **建议装**：GitHub 手机 App、Reddit App
- **不需要装**：任何代码编辑器、Git、Python

### Lexa（创始人）

- 已经全装了，跳过

## 平台账号注册顺序

如果你是新加入的宣发负责人，按这个顺序开账号：

1. **GitHub**（必须）
2. **TikTok**（必须，需要非中国手机号注册海外账号）
3. **Instagram**（必须）
4. **Reddit**（必须，注册后先养号 3-5 天再开始评论）

{: .important }
> TikTok 和 Instagram 账号开通前，先和 Lexa 对齐账号名、简介、头像。开了之后改名很麻烦。

## 工具相关的常见问题

### 我需要付费工具吗？
不需要。你的工作只用免费工具。HeyGen / OpenAI / Vercel 这些 Lexa 出钱。

### 我能用手机做所有事吗？
基本上可以。但审核脚本和写周报建议用电脑或平板，更舒服。

### 我能装更多工具来辅助吗？
可以，但不要把项目相关的内容放到没经过 Lexa 同意的工具里。

### 工具账号怎么交接？
所有账号注册时用项目共享邮箱（Lexa 提供）。这样后续交接不会丢账号。

## 相关页面

- [角色说明](./roles)：每个角色用什么工具
- [每周工作流](./workflow)：什么时候用什么工具
- [新人第一天](./day-one)：第一天要登录哪些工具
