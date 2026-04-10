---
title: FAQ
nav_order: 12
---

# FAQ

这里优先回答非技术 collaborator 最常问的问题。

## 项目相关

### Dayou 现在到底在做什么？

Dayou 现在是一个多仓库系统，不是单一项目。

- `mysterious`：主产品
- `animal-dayou`：宠物产品
- `dayou-content`：协作中台、内容资产和团队手册

如果你不确定自己该看哪个仓库，先看 [仓库分工](./repo-scope)。

### 我需要懂代码吗？

默认不需要。

大多数 collaborator 只需要会：

- 看文档
- 看 Issues
- 提 Issue
- 用自然语言和 AI 把问题整理清楚

### 我需要懂命令行或 Git 吗？

默认不需要。

### 我应该先配 GitHub，还是先配 AI？

两者都要，但 Dayou 现在默认是 `GitHub + 一个 AI 入口` 一起工作。

如果你还没配 AI，先看 [AI 配置](./ai-setup)。

### 我应该先看哪一页？

按这个顺序：

1. [AI 配置](./ai-setup)
2. [AI 接管入口](./ai-handoff)
3. [仓库分工](./repo-scope)
4. [每周工作流](./workflow)
5. [GitHub 零基础入门](./github-beginner-guide)

## AI 相关

### 我到底该用哪个 AI？

默认推荐顺序：

1. ChatGPT 或 Claude 网页版
2. Cursor
3. Codex / Claude Code

如果你只是想先参与协作，不要把“会不会本地 AI 工具”当成前置门槛。

### 我必须会 Cursor、Codex 或 Claude Code 吗？

默认不需要。

Dayou 真正需要的是：

- 你有一个 AI 入口
- 这个 AI 能读 Dayou 的页面
- 这个 AI 能帮你走后面的流程

### 我把哪个链接贴给 AI？

优先贴这个：

`https://dayouproject.github.io/dayou-content/ai-handoff.html`

或者直接打开 [AI 接管入口](./ai-handoff)。

### AI 读不了链接怎么办？

直接打开 [AI 接管入口](./ai-handoff)，把整页内容复制进去。

### gstack office hours 是日常入口吗？

不是。

它更像专项技术咨询入口。

默认顺序是：

1. 先让 AI 帮你整理问题
2. 再决定是否需要 office hours

### `/daily` 是什么？

这是 Dayou 希望 AI 统一支持的一个组织级动作：

- 读取当前上下文
- 压缩成今天的 daily
- 告诉你今天最重要的 3 件事和 blockers

如果你想让 AI 直接做这个，告诉它 `/daily` 即可。

## GitHub 相关

### 我注册好了 GitHub，下一步做什么？

把你的 GitHub 用户名发给 Lexa，接受对应仓库邀请，然后开始看文档和 Issues。

### 我不会写代码，也要用 GitHub 吗？

要，但你主要只用 GitHub 网页。

### 我需要 clone 仓库吗？

默认不需要。

### 我需要先开 Issue，还是先让 AI 帮我整理？

默认先让 AI 帮你整理，再开 Issue。

### Issue 模板没有显示怎么办？

- 先确认你打开的是仓库的 `Issues` 页面
- 再确认点的是 `New issue`
- 如果还是没有，直接把截图发给 Lexa

### 我写错了 Issue，可以改吗？

可以。打开你自己的 Issue，点右上角 `...`，选择编辑即可。

## 流程相关

### 我到底应该先找 AI，还是先找 Lexa？

默认顺序是：

1. 先看上下文
2. 先问 AI
3. 再开 Issue
4. 再让 Lexa 做技术判断

### 我该把需求提到哪个仓库？

先按这个判断：

- 改主产品：`mysterious`
- 改宠物产品：`animal-dayou`
- 改协作方式、文档、内容资产：`dayou-content`

如果还是不确定，先问 AI。

### 我应该把想法发到哪里？

正式版本发 GitHub Issue。  
微信只用来提醒紧急问题。

### 我什么时候该用 office hours？

当需求合理，但技术路径不清楚时。

比如：

- 自动化能不能做
- 现有技术栈是否合适
- 第一版最小可交付怎么切

### 我什么时候该用 `/daily`？

当你想让 AI 帮你把当前仓库上下文压缩成今天的行动清单时。

### 什么时候该直接找 Lexa？

这些情况不要自己硬撑：

- 你进不了 GitHub
- 你没权限看仓库
- 你看不到 Issue 模板
- 有当天必须处理的线上问题
- 支付、账号、上线出现风险

## 故障排查

### 我登不上 GitHub

- 先检查用户名、邮箱、密码
- 再试忘记密码
- 再看邮箱里有没有 GitHub 验证或安全邮件
- 还不行就把截图发给 Lexa

### 我点开仓库提示没有权限

- 先检查是否已接受邀请
- 退出后重新登录再试
- 还不行就把 GitHub 用户名发给 Lexa

### 手机上看页面不方便怎么办？

可以直接用手机浏览器，也可以装 GitHub App。

### 我不确定这件事是不是值得提 Issue

不要卡着。先问 AI，让 AI 帮你把“问题、目标、证据、done 标准”整理出来。

## 还有问题怎么办

- 紧急问题：微信
- 正式需求：GitHub Issue
- 不确定归属：先看 [仓库分工](./repo-scope)，再问 AI
- 不知道 AI 怎么配：看 [AI 配置](./ai-setup)
