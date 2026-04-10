# 协作规则 / Contributing

> **核心原则：只有 Lexa（创始人）能 push 到 main 分支。**
> **但所有团队成员都应该 clone 仓库到本地，用 Claude Code 跑 `/daily` 看自己的任务。**

这条规则适用于 Dayou 项目下的所有仓库：
- [mysterious](https://github.com/AlyciaBHZ/mysterious)（产品主仓库）
- [animal-dayou](https://github.com/AlyciaBHZ/animal-dayou)（宠物命理副产品）
- [dayou-content](https://github.com/AlyciaBHZ/dayou-content)（内容运营与团队协作）

---

## 团队成员的本地工作流

**clone 是为了方便你看项目状态和跑 `/daily`，不是为了 push 代码。**

### 第一次设置（5 分钟）

```bash
# 1. 装 Claude Code
# https://docs.claude.com/claude-code

# 2. clone 仓库到你电脑
git clone https://github.com/AlyciaBHZ/dayou-content.git
cd dayou-content

# 3. 在 Claude Code 里打开这个目录
claude code .

# 4. 跑 /daily 看你的当日任务
# 在 Claude Code 里输入：/daily
```

### 日常用法

每天来上班第一件事：

```bash
cd dayou-content
git pull origin main      # 同步最新变更
claude code .             # 打开 Claude Code
# 在 Claude Code 里：/daily
```

`/daily` 会根据你的 GitHub 用户名自动识别角色，告诉你：
- 本周脚本管线状态
- 你需要审核或回应的 Issue
- 接下来 3 天的发布排期
- 需要你做决定的事

### 提交工作的方式

你的工作产出**不通过 git push**，而是通过 GitHub Issues：

| 你要做的事 | 怎么做 |
|------|------|
| 提交内容概念 | 在 GitHub 网页或者 `gh issue create` 提 Content Idea Issue |
| 审核脚本 | 在对应 Issue 评论区写"通过 / 需改 / 拒绝" |
| 提交周报 | 提 Weekly Report Issue |
| 紧急情况 | 微信联系 Lexa |

**不要 `git commit` 任何东西。** 你的工作不需要写代码。

---

## 为什么不允许 push 到 main

| 原因 | 影响 |
|------|------|
| **部署一致性** | mysterious 和 animal-dayou 接 Vercel 自动部署，main 任何提交都会立即上线 |
| **部署门禁** | Vercel 要求 commit 作者邮箱是 GitHub 验证邮箱，否则部署失败 |
| **代码审查** | 任何人改产品代码前都需要 Lexa 看一眼 |
| **责任归属** | 出问题时能清楚追踪是谁的改动 |

---

## 如果你不小心运行了 git push

立即通知 Lexa（微信）。**不要尝试自己回滚。**

如果只是 push 失败（比如权限不够），不用担心，没造成任何影响。

---

## 给未来的技术开发者

如果你是开发者，需要改产品代码：

1. ✅ 创建新分支：`git checkout -b feature/your-task`
2. ✅ 改代码、commit
3. ✅ Push 你自己的分支：`git push origin feature/your-task`
4. ✅ 在 GitHub 上开 Pull Request，目标 `main`
5. ✅ 等 Lexa review 并 merge

**绝对不要：**
- ❌ `git push origin main`
- ❌ `git push --force` 任何分支
- ❌ 跳过 PR 直接 merge

### Git 邮箱配置

```bash
# 找到你的 GitHub noreply 邮箱：
# https://github.com/settings/emails
# 格式：<id>+<username>@users.noreply.github.com

git config --global user.email "你的-id+用户名@users.noreply.github.com"
git config --global user.name "你的GitHub用户名"
```

否则你 push 后 Vercel 会报：
> Deployment Blocked: The deployment was blocked because the commit author email is not valid.

---

## 紧急联系

| 情况 | 联系方式 |
|------|---------|
| Vercel 部署失败 | 微信 Lexa |
| GitHub Issue 看不到模板 | 微信 Lexa |
| `/daily` 跑不起来 | 微信 Lexa |
| 不小心改了不该改的东西 | 微信 Lexa |
| 一般问题 | GitHub Issue |

---

## 总结一句话

**Clone 仓库 + 跑 `/daily` 看任务是鼓励的。所有改动通过 GitHub Issues 提交。Lexa 是 main 分支的唯一守门人。**
