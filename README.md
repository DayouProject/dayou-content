# Dayou 协作中台 / Collaboration Hub

> Dayou 三个核心仓库的统一协作入口：仓库分工、团队手册、内容资产与协作工作流都从这里开始。

## 先看这个

如果你来这里是为了理解“这件事该在哪个仓库推进”，先看：

- `docs/repo-scope.md`
- `docs/workflow.md`
- `docs/github-beginner-guide.md`

这三个文件对应三件事：

1. 三个仓库各自负责什么
2. 想法如何变成正式 Issue，再进入实现
3. 零基础协作者如何上手 GitHub

## 三个核心仓库

| 仓库 | 核心 scope |
|------|------|
| [mysterious](https://github.com/DayouProject/mysterious) | 主产品、排盘、AI 解读、正式线上功能 |
| [animal-dayou](https://github.com/DayouProject/animal-dayou) | 宠物方向产品 |
| [dayou-content](https://github.com/DayouProject/dayou-content) | 协作中台、内容资产、团队手册 |

## 这是什么

`dayou-content` 仍然承载内容和知识资产，但它现在同时承担更高一层的作用：

- 统一说明三个仓库的边界
- 给不会写代码的 collaborator 提供入口
- 承载 GitHub Pages 团队手册
- 沉淀内容资产、知识库和流程文档

其中内容管线本身依然是这个仓库的重要组成部分。

一条自动化内容管线，把中国传统智慧（易经、道德经等）转化为 TikTok/Instagram 短视频，面向海外观众。

**工作流程：**
1. 从 `corpus/` 读取古典文本素材
2. AI 自动生成一周 7 条短视频脚本
3. 通过 HeyGen 生成 AI avatar 视频
4. 通过 n8n 自动发布到社交平台

## 团队协作

`dayou-content` 现在不只是内容仓库，也是 Dayou 三个核心仓库的协作中台。

默认协作方式：

1. 先判断需求属于哪个仓库
2. 先问 AI，把问题整理清楚
3. 再开 GitHub Issue
4. 由 Lexa 负责技术实现和收口

完全零基础？先看：

- [仓库分工](docs/repo-scope.md)
- [每周工作流](docs/workflow.md)
- [GitHub 零基础入门](docs/github-beginner-guide.md)

## 目录结构

```
dayou-content/
├── README.md              # 本文件
├── RUNBOOK.md              # 非技术人员操作手册
├── CULTURAL_TRANSLATION.md # 海外受众术语翻译规则
├── config.yaml             # 管线配置（LLM、HeyGen、发布调度）
├── team.yaml               # 团队成员与角色
├── corpus/                 # 古典文本语料库
│   ├── yijing/             # 易经
│   ├── daodejing/          # 道德经
│   └── wisdom/             # 独立智慧语录
├── scripts/                # 脚本生成模块
│   ├── generator.py        # AI 批量生成脚本
│   └── templates/          # 脚本格式模板
├── video/                  # 视频生成模块
│   └── heygen_client.py    # HeyGen API 客户端
├── publish/                # 发布模块
│   └── scheduler.py        # n8n webhook 发布
├── pipeline.py             # 主入口（CLI）
├── workspace/              # 运行时产出（脚本、视频、发布记录）
├── docs/                   # 文档
│   └── github-beginner-guide.md  # GitHub 零基础入门
└── .github/
    └── ISSUE_TEMPLATE/     # Issue 模板
        ├── content-idea.md     # 脚本概念提交
        └── weekly-report.md    # 周报
```

## 快速开始（技术人员）

```bash
# 克隆仓库
git clone https://github.com/DayouProject/dayou-content.git
cd dayou-content

# 安装依赖
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 设置 API 密钥
export OPENAI_API_KEY="..."
export HEYGEN_API_KEY="..."
```

## 常用命令

```bash
# 生成一周的脚本
python3 pipeline.py generate

# 生成视频（需要 HeyGen API key）
python3 pipeline.py video --wait

# 发布到社交平台（需要 n8n webhook）
python3 pipeline.py publish

# 全流程（生成 → 视频 → 发布）
python3 pipeline.py full
```

## 配置

所有配置在 `config.yaml` 中：

| 配置项 | 说明 |
|--------|------|
| `corpus` | 语料库来源和权重 |
| `llm` | AI 模型设置（OpenAI 兼容） |
| `heygen` | Avatar 视频生成设置 |
| `publish` | 发布平台和时间表 |
| `persona` | Avatar 人设（The Sage） |
| `n8n` | 自动发布 webhook |

## 相关项目

| 项目 | 说明 |
|------|------|
| [mysterious](https://github.com/DayouProject/mysterious) | 大有主产品（排盘 + AI 解读） |
| [animal-dayou](https://github.com/DayouProject/animal-dayou) | 宠物命理（楔子产品） |
| [omega-ancient-texts-analysis](https://github.com/ChronoAIProject/omega-ancient-texts-analysis) | 参考架构：古典文本 AI 分析管线 |
