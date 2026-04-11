---
title: AI 配置
nav_order: 2
---

# AI 配置

这页只回答四件事：

1. **完全零基础**怎么从零装好第一个 AI 客户端
2. Dayou 最低要求你配哪一种 AI 客户端
3. 什么叫"已经配置完成"
4. 配完以后，下一步该把哪个链接贴给 AI

## 完全零基础？从这里开始

如果你电脑上没有任何 AI 工具，从来没有用过 ChatGPT 命令行版，没有打开过 terminal，那这一节就是为你写的。**预计时间：30 分钟。** 跟着每一步做，不要跳。

### 第 0 步：你需要先做的小决定

下面三种工具，**你只需要选一个开始**。看完简介选一个，剩下的不用管。

| 工具 | 长什么样 | 月费 | 谁适合 |
|------|--------|------|------|
| **Claude（推荐零基础）** | 像 ChatGPT 那样的网页对话 + 一个命令行版 Claude Code | $20/月 Pro 套餐 | 完全没有任何编程经验、只想用浏览器和命令行的人 |
| **Cursor** | 一个长得像 VS Code 的应用，里面内置 AI | $20/月 Pro 套餐 | 已经写过一点代码、习惯有"图形界面 + 文件树"的人 |
| **Codex (OpenAI)** | OpenAI 出的命令行工具，配合 ChatGPT 订阅 | 需要 ChatGPT Plus $20/月 | 已经习惯命令行、贴近代码工作的人 |

**真的不知道选哪个？选 Claude。** 这一节后面的步骤就以 Claude 为例。

### 第 1 步：打开订阅页面

1. 用电脑浏览器打开 <https://claude.ai>
2. 点右上角 "Sign up"，用邮箱注册
3. 注册成功后回到 <https://claude.ai>，点页面里的 "Upgrade plan" 或 "Get Pro"
4. 选 **Claude Pro $20/月** 套餐，按提示填信用卡完成订阅
5. 完成后你会看到一个对话框，左侧能看到聊天历史 — 这就是网页版 Claude

> 如果你只想试一下不订阅，免费版也能用，但每天有用量限制，并且不支持 Claude Code 命令行。Dayou 协作流程要求 Pro 才稳定。

### 第 2 步：装命令行版（Claude Code）

Claude Code 是 Claude 的命令行工具，Dayou 的 agent 流程需要它。

#### 如果你是 Mac 用户

1. 按 **Command + 空格** 打开 Spotlight 搜索
2. 输入 `terminal`，回车，Mac 会打开"终端"应用（一个黑底白字的窗口）
3. 在这个窗口里粘贴下面这一行，按回车：
   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```
4. 按提示完成安装（可能要求输入密码，就是你 Mac 的开机密码）
5. 安装完成后关掉终端窗口，**重新打开**一个新的终端窗口
6. 在新窗口里输入 `claude --version`，按回车
7. 如果显示一串版本号（比如 `claude 1.x.x`），说明装好了

#### 如果你是 Windows 用户

1. 按 **Win 键**，搜索 `PowerShell`，点开 "Windows PowerShell"
2. 在窗口里粘贴下面这一行，按回车：
   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```
3. 按提示完成安装
4. 关掉 PowerShell 窗口，**重新打开**一个新的
5. 在新窗口里输入 `claude --version`，回车
6. 看到版本号就成功了

> 如果上面的命令报错，最稳的备用路径是直接装 Cursor。Cursor 是一个 GUI 应用，去 <https://cursor.com> 下载安装包，双击运行就行。下面第 3 步换成"在 Cursor 里开新对话"即可。

### 第 3 步：第一次跟 Claude Code 对话

1. 在终端（Mac 的 Terminal 或 Windows 的 PowerShell）里输入：
   ```bash
   claude
   ```
2. 回车
3. 第一次会要求你登录，按提示在浏览器里完成
4. 登录完成后回到终端，会看到一个提示符，让你输入第一个问题
5. 输入下面这段话，按回车：

```text
你好。我是 Dayou 团队的协作者。请先帮我读这个页面，然后告诉我接下来该做什么：
https://dayouproject.github.io/dayou-content/
```

6. Claude Code 会读这个页面，然后用普通中文告诉你下一步

**到这里你已经配置完成了。** 后面的事都让 AI 带着你走。

### 第 4 步：日常怎么继续

每次你想跟 Dayou AI 协作，只需要：

1. 打开终端
2. 输入 `claude`
3. 把任何 Dayou 页面链接、Issue 链接、问题描述粘贴进去
4. AI 会按 Dayou 的流程带你走

你不需要会写代码，也不需要自己研究 Node.js、Vercel 这些开发工具。  
但如果你要在仓库里直接跑 `/daily`，AI 必须先带你完成 `gh auth` 和三个 Dayou 仓库的 clone。

### 这一节的配置完成标志

- [ ] 你的 Claude 订阅或同等订阅是激活的
- [ ] 你的电脑能打开终端（Mac Terminal 或 Win PowerShell）
- [ ] `claude --version` 能在终端里跑出版本号
- [ ] `claude` 命令能进入对话模式
- [ ] 你能把一个链接粘贴进去并让 AI 读它

如果上面五项里有任何一项不通，**直接微信 Lexa 截图发问**。不要自己卡半天。

---

## 先讲结论

Dayou 现在的最低标准不是“任意 AI 都行”。

每个 collaborator 至少要配置下面三者之一：

1. Claude
2. Cursor
3. Codex

原因不是为了统一品牌，而是为了统一能力：

- 先用 AI 整理问题
- 先让 AI 准备 `office hours brief`
- 再把结果变成 `repo 路由 / GitHub Issue 草稿 / /daily`

`gstack office hours` 不是替代品。  
它建立在你已经有 `Claude / Cursor / Codex` 其中之一的前提上。

ChatGPT 可以作为补充工具，但不再作为 Dayou 的团队最低标准。

## 你该选哪条路

| 你的情况 | 推荐选择 | 原因 |
|---|---|---|
| 完全不会代码，只想先参与协作 | Claude | 浏览器即可，最轻，最适合先跑通 Dayou 流程 |
| 已经在用编辑器，想把 AI 放在一个熟悉的地方 | Cursor | 适合已经有编辑器习惯的人 |
| 已经能用更贴近 repo 的工作方式 | Codex | 更适合和实现层衔接 |
| 想确认技术栈是否合理、想问系统级问题 | gstack office hours | 这是专项咨询，不是替代 AI 客户端 |

## 先统一最低标准，再统一行为

不同客户端的按钮和界面会变，但 Dayou 真正关心的是这五个结果：

1. 你至少已经有 `Claude / Cursor / Codex` 之一
2. 你能开一个新的干净对话
3. 你能把链接或文字喂给 AI
4. AI 能用普通中文回答你
5. AI 能帮你产出 `repo 路由 / office hours 准备 / /daily / Issue 草稿`

如果你已经 clone 了仓库，最好直接让它用 repo-native 命令：

- `/route`
- `/context`
- `/issue`
- `/office-hours`
- `/daily`
- `/next`

如果这五件事都做到了，就算配置完成。

## 配置完成的标准

你的 AI 满足下面这张表，就可以进入 Dayou 工作流：

| 检查项 | 通过标准 |
|---|---|
| 账号可用 | 你能正常登录，不会频繁被卡在权限或订阅问题 |
| 客户端符合最低标准 | 你用的是 `Claude / Cursor / Codex` 其中之一 |
| 能开新对话 | 你能针对不同主题单独开新 chat |
| 能读链接或读粘贴文本 | 你能把 Dayou 页面链接或页面内容喂给 AI |
| 能输出中文结构化结果 | 它能给你 repo 判断、Issue 草稿、daily 草稿 |
| 能连续跟进同一话题 | 它不会第一轮说清楚，第二轮就完全忘掉目标 |

## 三条 AI 路线怎么理解

### 1. Claude

这是 Dayou 当前最推荐的大众路线，也是最轻的达标方式。

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

### 3. Codex

这是更贴近 repo 和实现层的路线。

如果你已经会用，可以继续用；如果你不会，也不必把它当成唯一入口。

对新人来说，先把“Claude / Cursor / Codex 之一 + AI 路由 + Issue 留痕”跑通，更重要。

## gstack office hours 在这套体系里的位置

这不是日常 AI 入口，而是专项技术判断入口。

它不是用来替代 `Claude / Cursor / Codex` 的，而是建立在它们之上的第二层：

1. 先用 `Claude / Cursor / Codex` 之一把问题整理清楚
2. 再让 AI 产出 `office hours brief`
3. 再去问 gstack

这里的 `gstack` 指官方 repo `garrytan/gstack`，不是 Dayou 自己发明的泛称：

- 官方地址：<https://github.com/garrytan/gstack>
- Claude Code：按官方 README 装到 `~/.claude/skills/gstack`
- Cursor：按官方 README 用 `./setup --host cursor`
- Codex：按官方 README 用 `./setup --host codex`
- Dayou 的要求不是“你自己手动背命令”，而是让 agent 先检测，缺了就补装

按官方说明，Windows 机器还要准备 `Node.js`；`gstack` 的 setup 会继续处理 host 对应的安装。

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

默认把我当成已经至少配好 Claude、Cursor 或 Codex 之一、但不会写代码的 collaborator。
不要一上来让我装本地开发工具。
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

1. 打开 [AI 接管入口](./ai-handoff.html)
2. 把页面内容整段复制进 AI
3. 再让它继续带你走流程

## 相关页面

- [AI 接管入口](./ai-handoff.html)
- [gstack Office Hours](./gstack-office-hours.html)
- [/daily 模板](./daily.html)
- [组织级 AI Skills](./organization-skills.html)
- [工具清单](./tools.html)
- [GitHub 零基础入门](./github-beginner-guide.html)
