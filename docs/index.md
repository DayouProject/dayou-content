---
title: 首页
nav_order: 1
layout: default
has_toc: false
---

<div class="hero-shell">
  <p class="portal-kicker">Execution First</p>
  <h1 class="hero-title">Dayou 一页执行入口</h1>
  <p class="hero-lead">
    人默认只需要读这一页。
    先配好 Claude、Cursor 或 Codex 之一，
    然后把这个首页链接交给你的 agent。
    它必须先完成 GitHub access、`gh auth`、clone 三个仓库、读取上下文，
    然后才能继续做 repo 路由、office hours、/daily、Issue 草稿。
  </p>
  <div class="hero-actions">
    <a class="portal-button primary" href="#copy-link">复制首页链接</a>
    <a class="portal-button secondary" href="#agent-order">看执行顺序</a>
    <a class="portal-button secondary" href="https://github.com/DayouProject/dayou-content/issues/new/choose">直接开 Issue</a>
  </div>
  <div class="signal-grid">
    <div class="signal-card">
      <span class="signal-label">最低门槛</span>
      <strong>GitHub + Claude / Cursor / Codex</strong>
      <p>每个人至少配好三者之一。默认不要求你先会代码，但要求你把基础协作环境配完整。</p>
    </div>
    <div class="signal-card">
      <span class="signal-label">默认入口</span>
      <strong>复制首页链接给 Agent</strong>
      <p>不是先复制一大段 prompt。默认先把这个首页链接交给 agent，让它按这里的顺序执行。</p>
    </div>
    <div class="signal-card">
      <span class="signal-label">不能跳步</span>
      <strong>先 gh auth，再 clone，再读上下文</strong>
      <p>没有完成这三层之前，不要直接开始 office hours、/daily 或正式 Issue 草稿。</p>
    </div>
  </div>
</div>

<div class="rule-banner">
  <span class="section-kicker">Core Rule</span>
  <p>Dayou 的默认模式不是“想到什么就立刻问 office hours”，而是“先完成 GitHub auth 和 repo context，再进入路由、判断和正式留痕”。</p>
</div>

## 复制这个首页链接给你的 Agent

这是默认入口。大多数协作者不需要先读别的页。

<div id="copy-link"></div>

```text
https://dayouproject.github.io/dayou-content/
```

如果你的 agent 需要一句起始指令，就复制这段：

```text
请先完整阅读并严格按顺序执行这个 Dayou onboarding 页面，不要跳步骤：
https://dayouproject.github.io/dayou-content/
```

## Agent 必须按这个顺序执行

<div id="agent-order"></div>

1. 先确认我已经有 `Claude / Cursor / Codex` 之一，并且能正常打开新对话或 agent。
2. 先确认我有 GitHub 账号，并且已经接受 Dayou 仓库邀请。
3. 先检查 `gh` 是否可用，再完成 `gh auth`。
4. 先 clone 三个仓库：`mysterious`、`animal-dayou`、`dayou-content`。
5. 先读取三个仓库的 `README`、`TODO`、open Issues。
6. 先用普通中文告诉我 Dayou 现在在做什么、三个仓库分别负责什么。
7. 只有在前面都完成以后，才继续做 `/route`、`/context`、`/office-hours`、`/daily`、`/issue`。

如果任何一步卡住，先解决这一步，不要往后跳。

## clone 后怎么直接用 Dayou skills

如果你已经在本地打开了任意一个 Dayou 仓库：

- Claude Code：直接输入 `/route`、`/context`、`/issue`、`/office-hours`、`/daily`、`/next`
- Cursor：直接输入 `/route`、`/context`、`/issue`、`/office-hours`、`/daily`、`/next`
- Codex：直接用自然语言触发同一套命令语义，比如 `给我一个今天的 /daily`

这三种入口现在都会先检查：

- `gh auth` 是否完成
- 三个仓库是否都在本地
- `README / TODO / open Issues` 是否已经读过

然后才输出对应结果。

## Agent 的最小命令顺序

如果你是 agent，默认先按这个顺序检查：

```bash
gh --version
gh auth status
gh auth login
gh repo clone DayouProject/mysterious
gh repo clone DayouProject/animal-dayou
gh repo clone DayouProject/dayou-content
```

完成以后，再去看：

- 三个仓库的 `README`
- 三个仓库的 `TODO`
- 三个仓库当前的 open Issues

如果私有仓库 clone 失败，不要跳过，先停下来确认：

- 用户是否已经接受 GitHub 邀请
- 用户是否真的有对应仓库权限
- 需要时先找 Lexa 补权限

## 三个仓库一句话记住

<div class="repo-grid">
  <div class="repo-card">
    <span class="repo-tag">主产品</span>
    <h2>mysterious</h2>
    <p>排盘、AI 解读、线上功能、转化、自动化、用户体验。凡是直接影响主产品的需求，优先去这里。</p>
  </div>
  <div class="repo-card">
    <span class="repo-tag">宠物产品</span>
    <h2>animal-dayou</h2>
    <p>宠物方向的功能、体验、反馈、增长。只要需求核心对象是宠物产品，就不要混到主产品仓库里。</p>
  </div>
  <div class="repo-card">
    <span class="repo-tag">协作中台</span>
    <h2>dayou-content</h2>
    <p>协作规则、团队手册、内容资产、知识文档、统一入口。这里解决的是“大家怎么对齐”。</p>
  </div>
</div>

## 只有 setup 完成后，Agent 才应该帮你做这些

- `/route`：判断该进哪个 repo
- `/context`：把 README / TODO / open Issues 解释成普通中文
- `/office-hours`：准备 gstack office hours brief
- `/daily`：基于当前上下文生成今天的 daily
- `/issue`：整理成可直接提交的 GitHub Issue 草稿

`/office-hours` 不是第一步。  
它只能出现在：问题已经整理清楚，但技术路径仍然不确定的时候。

## 贴进去以后，你只要这样说

不要再想“我下一步该看哪页”。直接对你的 agent 说事。

- `先帮我完成 Dayou 的 setup，不要跳步骤。`
- `先检查我的 gh auth 和三个仓库 clone 状态。`
- `先读完三个仓库的 README、TODO、open Issues，再告诉我现在在做什么。`
- `帮我判断这个需求该进哪个 repo。`
- `把这个需求整理成可以去问 gstack office hours 的 brief。`
- `给我一个今天的 /daily。`
- `把这个想法整理成 GitHub Issue 草稿。`

## 什么一定要回 GitHub

agent 可以整理，但不能替代正式留痕。

- 正式需求
- 正式决定
- office hours 之后的结论
- 实现进度
- 验收结果

## 只有这些情况才需要跳出这一页

- 你还没配好 Claude、Cursor、Codex 之一：看 [AI 配置](./ai-setup.html)
- 你想看 office hours 的标准模板：看 [gstack Office Hours](./gstack-office-hours.html)
- 你想看 `/daily` 的标准模板：看 [/daily 模板](./daily.html)
- 你进不了 GitHub、没权限、`gh auth` 失败、clone 不下来私有仓库：直接找 Lexa
