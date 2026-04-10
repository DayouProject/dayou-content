---
title: 首页
nav_order: 1
layout: default
has_toc: false
---

<div class="hero-shell">
  <p class="portal-kicker">One Page Start</p>
  <h1 class="hero-title">Dayou 一页上手</h1>
  <p class="hero-lead">
    人默认只需要读这一页。
    先配好 Claude、Cursor 或 Codex 之一，
    然后把下面的 Dayou Agent Bootstrap 复制到你的 agent 里。
    剩下的 repo 路由、office hours、/daily、Issue 草稿，都让它继续帮你执行。
  </p>
  <div class="hero-actions">
    <a class="portal-button primary" href="#copy-pack">复制给 Agent</a>
    <a class="portal-button secondary" href="#three-steps">看 3 步流程</a>
    <a class="portal-button secondary" href="https://github.com/DayouProject/dayou-content/issues/new/choose">直接开 Issue</a>
  </div>
  <div class="signal-grid">
    <div class="signal-card">
      <span class="signal-label">最低门槛</span>
      <strong>GitHub + Claude / Cursor / Codex</strong>
      <p>每个人至少配好三者之一。默认不要求你会代码，也不要求你先装本地开发环境。</p>
    </div>
    <div class="signal-card">
      <span class="signal-label">只读一页</span>
      <strong>不用先翻完整站</strong>
      <p>正常协作先读这一页就够了。其他页面是补充，不是默认起点。</p>
    </div>
    <div class="signal-card">
      <span class="signal-label">正式留痕</span>
      <strong>Agent 整理，GitHub 定稿</strong>
      <p>聊天可以先走 agent，但正式需求、决定、验收结论最后都要回到 GitHub Issue。</p>
    </div>
  </div>
</div>

<div class="rule-banner">
  <span class="section-kicker">Core Rule</span>
  <p>Dayou 的默认模式不是“人先学工具”，而是“人用自然语言说清楚，agent 帮你整理并推进，正式版本回到 GitHub”。</p>
</div>

<section class="section-block" id="three-steps">
  <div class="section-head">
    <span class="section-kicker">Three Steps</span>
    <h2>你只需要做 3 步</h2>
    <p>不要先把自己扔进很多页面，也不要先研究代码。先把这三步跑通。</p>
  </div>
  <div class="flow-grid">
    <div class="flow-card">
      <span class="step-number">01</span>
      <h3>配一个标准客户端</h3>
      <p>先配好 Claude、Cursor 或 Codex 之一。ChatGPT 可以补充用，但不再是团队最低标准。</p>
    </div>
    <div class="flow-card">
      <span class="step-number">02</span>
      <h3>把 Bootstrap 复制到你的 Agent</h3>
      <p>新开一个 agent 或新对话，把下面整段 Dayou Agent Bootstrap 粘进去，让它进入 Dayou 协作模式。</p>
    </div>
    <div class="flow-card">
      <span class="step-number">03</span>
      <h3>直接说你要推进什么</h3>
      <p>之后你只需要用普通中文说需求、问题、计划或 blocker。它应该继续帮你判断 repo、准备 office hours、生成 /daily 或 Issue 草稿。</p>
    </div>
  </div>
</section>

## 复制到你的 Agent

这是默认入口。大多数协作者不需要先继续读别页。

| 你在用什么 | 你现在做什么 |
|---|---|
| Claude | 开一个新对话或新 project，把下面整段粘进去 |
| Cursor | 开一个新的 agent chat，把下面整段粘进去 |
| Codex | 开一个新的 agent，把下面整段当作起始指令 |

<div id="copy-pack"></div>

```text
你现在是 Dayou collaborator agent。

你的目标不是直接写代码，而是帮助我用自然语言推进 Dayou 的正式工作。
默认把我当成不会写代码、但已经配好 Claude / Cursor / Codex 之一的人。

你先做这 4 件事：
1. 先用普通中文总结 Dayou 三个仓库的区别
2. 再问我最多 3 个问题
3. 判断我现在更需要 `/route`、`/office-hours`、`/daily`、`/issue` 里的哪一种
4. 产出结构化结果，并提醒我把正式版本回到 GitHub Issue

Dayou 的稳定上下文：
- mysterious：主产品，排盘、AI 解读、线上功能、自动化、增长、用户体验
- animal-dayou：宠物方向产品
- dayou-content：协作中台、团队手册、内容资产、知识文档、统一入口

你必须遵守这些规则：
- 不要假定固定岗位
- 不要默认我会本地开发
- 不要一上来让我装 git、Node.js、Vercel、Claude Code 或别的本地工具
- gstack office hours 不是第一步
- 只有在问题已经整理清楚、但技术路径仍然不确定时，才进入 `/office-hours`
- 所有正式需求、正式决定、验收结论，最后都要回到 GitHub Issue

你要支持这 5 种动作：
- `/route`：帮我判断该进哪个 repo
- `/context`：把 README / TODO / open Issues 解释成普通中文
- `/office-hours`：帮我准备 gstack office hours brief
- `/daily`：基于当前上下文生成今天的 daily
- `/issue`：把想法整理成可直接提交的 GitHub Issue 草稿

你的输出要求：
- 全程用普通中文
- 先复述我的问题，再问问题，再给结论
- 输出尽量结构化、短、清楚

现在先开始：
先用普通中文总结 Dayou 三个仓库的区别，再问我最多 3 个问题，判断我现在更需要什么。
```

## 贴进去以后，你只要这样说

不要再想“我下一步该看哪页”。直接对你的 agent 说事。

- `帮我判断这个需求该进哪个 repo。`
- `把这个需求整理成可以去问 gstack office hours 的 brief。`
- `给我一个今天的 /daily。`
- `把这个想法整理成 GitHub Issue 草稿。`
- `把 mysterious 当前的 README、TODO、open Issues 用普通中文讲给我。`

<section class="section-block">
  <div class="section-head">
    <span class="section-kicker">Three Repos</span>
    <h2>三个仓库一句话记住</h2>
    <p>agent 默认也应该按这个边界帮你路由。</p>
  </div>
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
</section>

## 什么一定要回 GitHub

这条要记住。agent 可以整理，但不能替代正式留痕。

- 正式需求
- 正式决定
- office hours 之后的结论
- 实现进度
- 验收结果

## 只有这些情况才需要跳出这一页

- 你还没配好 Claude、Cursor、Codex 之一：看 [AI 配置](./ai-setup.html)
- 你想看 office hours 的标准模板：看 [gstack Office Hours](./gstack-office-hours.html)
- 你想看 `/daily` 的标准模板：看 [/daily 模板](./daily.html)
- 你进不了 GitHub、没权限、看不到模板：直接找 Lexa
