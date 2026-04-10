---
title: 首页
nav_order: 1
layout: default
has_toc: false
---

<div class="hero-shell">
  <p class="portal-kicker">Human Language First</p>
  <h1 class="hero-title">Dayou 协作门户</h1>
  <p class="hero-lead">
    三个核心仓库的统一入口。先判断事情属于哪个仓库，再把自然语言需求整理成正式 Issue，最后进入实现、上线和验证。
    这里默认你不写代码，也默认你可以先用 AI 把问题问清楚。
  </p>
  <div class="hero-actions">
    <a class="portal-button primary" href="./repo-scope">先判断去哪个仓库</a>
    <a class="portal-button secondary" href="./workflow">看标准工作流</a>
    <a class="portal-button secondary" href="./github-beginner-guide">零基础协作怎么开始</a>
  </div>
  <div class="signal-grid">
    <div class="signal-card">
      <span class="signal-label">默认工具</span>
      <strong>浏览器 + GitHub + AI</strong>
      <p>不需要 clone 仓库，不需要本地开发环境，不需要先学代码。</p>
    </div>
    <div class="signal-card">
      <span class="signal-label">正式留痕</span>
      <strong>所有结论回到 Issue</strong>
      <p>微信可以提醒，AI 可以帮你整理，但正式决定、需求、验收都回到 GitHub Issue。</p>
    </div>
    <div class="signal-card">
      <span class="signal-label">三个仓库</span>
      <strong>平级分工，不是主次</strong>
      <p>`mysterious`、`animal-dayou`、`dayou-content` 同等重要，只是解决的问题不同。</p>
    </div>
  </div>
</div>

<div class="rule-banner">
  <span class="section-kicker">Core Rule</span>
  <p>模糊想法可以先和 AI 讨论，但团队真正采用什么、做什么、什么时候做，必须留在 GitHub Issue 里，不能只停留在聊天窗口。</p>
</div>

<section class="section-block">
  <div class="section-head">
    <span class="section-kicker">Three Scopes</span>
    <h2>先判断你的事情该进哪个仓库</h2>
    <p>Dayou 现在不是单仓库工作方式。先判断归属，后面的讨论、优先级和实现才不会跑偏。</p>
  </div>
  <div class="repo-grid">
    <a class="repo-card" href="https://github.com/DayouProject/mysterious">
      <span class="repo-tag">主产品</span>
      <h2>mysterious</h2>
      <p>排盘、AI 解读、线上功能、转化、自动化、用户体验。凡是直接影响主产品的需求，优先去这里。</p>
    </a>
    <a class="repo-card" href="https://github.com/DayouProject/animal-dayou">
      <span class="repo-tag">宠物产品</span>
      <h2>animal-dayou</h2>
      <p>宠物方向的功能、体验、反馈、增长。只要需求核心对象是宠物产品，就不要混到主产品仓库里。</p>
    </a>
    <a class="repo-card" href="https://github.com/DayouProject/dayou-content">
      <span class="repo-tag">协作中台</span>
      <h2>dayou-content</h2>
      <p>协作规则、团队手册、内容资产、知识文档、统一入口。这里解决的是“大家怎么对齐”。</p>
    </a>
  </div>
</section>

<section class="section-block">
  <div class="section-head">
    <span class="section-kicker">Common Starts</span>
    <h2>你现在大概率属于这四种状态之一</h2>
    <p>不用先想技术细节，先找到你当前的入口。</p>
  </div>
  <div class="triage-grid">
    <div class="triage-card">
      <h3>我有一个新想法</h3>
      <p>先用 AI 或 gstack 把问题、目标、done 标准整理清楚，再开正式 Issue。</p>
    </div>
    <div class="triage-card">
      <h3>我发现一个问题</h3>
      <p>先确认影响的是哪个仓库，再把现象、证据、截图、链接放进对应 Issue。</p>
    </div>
    <div class="triage-card">
      <h3>我不知道该去哪</h3>
      <p>先看仓库分工。如果还不确定，先问 AI 帮你判断归属，再去最相关的仓库留痕。</p>
    </div>
    <div class="triage-card">
      <h3>我不会 GitHub</h3>
      <p>直接看零基础入门。默认模式就是浏览器协作，不要求你装本地工具链。</p>
    </div>
  </div>
</section>

<section class="section-block">
  <div class="section-head">
    <span class="section-kicker">Workflow</span>
    <h2>标准协作流程只有五步</h2>
    <p>它的重点不是流程感，而是让上下文、判断和结果都可追踪。</p>
  </div>
  <div class="flow-grid">
    <div class="flow-card">
      <span class="step-number">01</span>
      <h3>先看上下文</h3>
      <p>看目标仓库的 README、TODO 和 open Issues，避免重复提需求，也避免问一个已经在做的问题。</p>
    </div>
    <div class="flow-card">
      <span class="step-number">02</span>
      <h3>先问 AI</h3>
      <p>先把问题范围、可行性、最小版本和 done 标准整理出来，不让模糊想法直接进仓库。</p>
    </div>
    <div class="flow-card">
      <span class="step-number">03</span>
      <h3>提交正式 Issue</h3>
      <p>把问题、目标、证据、优先级理由、AI 判断都写进去，让需求从聊天变成系统的一部分。</p>
    </div>
    <div class="flow-card">
      <span class="step-number">04</span>
      <h3>Lexa 决策并实现</h3>
      <p>是否做、什么时候做、技术怎么落地，都在同一个 Issue 里持续更新。</p>
    </div>
    <div class="flow-card">
      <span class="step-number">05</span>
      <h3>回到原 Issue 验证</h3>
      <p>上线和验收也回到原地，不让需求在私聊里结案。</p>
    </div>
  </div>
</section>

<section class="section-block">
  <div class="section-head">
    <span class="section-kicker">Reading Path</span>
    <h2>20 分钟内完成上手</h2>
    <p>如果你是第一次加入，按这个顺序读就够了。</p>
  </div>
  <div class="reading-grid">
    <div class="reading-card">
      <h3><a href="./repo-scope">仓库分工</a></h3>
      <p>先把三个仓库的职责边界看清楚，减少后续来回搬运。</p>
    </div>
    <div class="reading-card">
      <h3><a href="./workflow">每周工作流</a></h3>
      <p>看一个想法如何从自然语言进入正式系统，再进入实现和验证。</p>
    </div>
    <div class="reading-card">
      <h3><a href="./github-beginner-guide">GitHub 零基础入门</a></h3>
      <p>只讲注册、接受邀请、提交 Issue 这些真正需要的动作。</p>
    </div>
    <div class="reading-card">
      <h3><a href="./faq">FAQ</a></h3>
      <p>权限、手机协作、Issue 用法、是否需要本地工具，这里一次看清楚。</p>
    </div>
  </div>
</section>

<section class="section-block">
  <div class="section-head">
    <span class="section-kicker">Quick Links</span>
    <h2>直接去需要的地方</h2>
  </div>
  <div class="reading-grid">
    <div class="reading-card">
      <h3><a href="./tools">工具清单</a></h3>
      <p>默认需要什么，不需要什么，哪些工具只是可选增强。</p>
    </div>
    <div class="reading-card">
      <h3><a href="./day-one">新人第一天</a></h3>
      <p>给第一次加入的人一条最短上手路径，不靠经验传承。</p>
    </div>
    <div class="reading-card">
      <h3><a href="./next-steps">接下来 2 周</a></h3>
      <p>看现在团队正在推进什么，避免提一个已经被排进去的需求。</p>
    </div>
    <div class="reading-card">
      <h3><a href="https://github.com/DayouProject/dayou-content/issues/new/choose">新建 Issue</a></h3>
      <p>已经判断清楚并整理完需求后，直接从这里进入正式留痕。</p>
    </div>
  </div>
</section>
