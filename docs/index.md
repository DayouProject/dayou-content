---
title: 首页
nav_order: 1
layout: default
has_toc: false
---

# Dayou 内容运营中台

Dayou 是一个面向海外市场的中国形而上学 AI 平台；这个仓库负责把知识库概念稳定转成可发布的短视频内容。

## 3 人协作总图

```text
[知识库负责人]
    |
    | [concepts]
    v
[Lexa/Pipeline]
    |
    | [scripts+videos]
    v
[宣发负责人]
    |
    | [TikTok / Instagram / Reddit]
    v
[数据与反馈]
```

这不是写代码仓库介绍页。这里讲 3 件事：谁负责、怎么交接、这一周先做什么。

## 谁负责什么

| 角色 | 负责什么 | 明确不负责什么 | 主要工作区 | 什么时候出手 |
|---|---|---|---|---|
| Lexa（AlyciaBHZ） | 内容管线、`pipeline.py`、`dayou.dev`、Vercel、HeyGen、n8n、周节奏与策略 | 不长期写内容，不运营 TikTok/Instagram，不做日常 Reddit 互动 | 本仓库、终端、Vercel、HeyGen、n8n | 周一接收概念，周二到周四产脚本和视频，异常时随时介入 |
| 知识库负责人（TBD） | 每周内容概念、脚本准确性审核、文化翻译质量、主知识库维护 | 不改代码，不部署，不跑管线，不管理社媒账号 | GitHub Issue、仓库文档、微信 | 周一前交概念，周二到周三审脚本，周日补知识库修订 |
| 宣发负责人（TBD） | TikTok/Instagram 发布执行、Reddit 社区互动、数据跟踪、周报 | 不改代码，不部署，不跑管线，不替知识库做文化判断 | TikTok、Instagram、Reddit、GitHub Issue | 周四接视频，周五到周日发布、互动、复盘 |

## 本周优先动作

| 角色 | 本周先做什么 | 做到什么程度算完成 |
|---|---|---|
| Lexa | 开通 HeyGen 并做 Avatar；跑通前 3 条视频的端到端流程；配置 TikTok Business | 至少 3 条视频从概念走到成片；账号与工具均可登录；发布链路不再卡在账号侧 |
| 知识库负责人 | 注册 GitHub；读完 [CULTURAL_TRANSLATION.md](https://github.com/AlyciaBHZ/dayou-content/blob/main/CULTURAL_TRANSLATION.md)；提交首个含 3 个概念的 Content Idea Issue | Issue 信息完整，可直接进入脚本生成；每个概念都有经典来源、现代角度、禁区提醒 |
| 宣发负责人 | 注册 GitHub；开好 TikTok/Instagram 账号；准备手动发布首批测试视频 | 两个平台账号可用；已拿到后台权限；能手动发布并记录链接与基础数据 |

## 读文档顺序

新加入的人先按这个顺序读：

1. [角色说明](./roles)：先弄清楚自己负责什么，不负责什么。
2. [每周工作流](./workflow)：再看交接顺序、异常处理和沟通规则。
3. [接下来 2 周](./next-steps)：最后直接看自己这两周要交什么。

第一次用 GitHub 的同学，在第 1 步之前先看 [GitHub 零基础入门](./github-beginner-guide)。

## 现在就用哪些入口

| 目的 | 去哪里 | 输出什么 |
|---|---|---|
| 提交内容概念 | GitHub Issue | 1 个 Content Idea Issue，内含 2 到 3 个概念 |
| 审核脚本 | GitHub Issue + `workspace/scripts/` | 明确写“通过 / 需改 / 拒绝”，并指出具体句子 |
| 接收视频并发布 | GitHub Issue + `workspace/videos/` + 平台后台 | 发布链接、发布时间、异常记录 |
| 紧急同步 | 微信 | 只处理今天必须解决的事，之后补回 Issue |

## 相关页面

- [角色说明](./roles)
- [每周工作流](./workflow)
- [接下来 2 周](./next-steps)
- [FAQ](./faq)
- [GitHub 零基础入门](./github-beginner-guide)
- [RUNBOOK.md（GitHub）](https://github.com/AlyciaBHZ/dayou-content/blob/main/RUNBOOK.md)
- [直接新建 Issue](https://github.com/AlyciaBHZ/dayou-content/issues/new/choose)
