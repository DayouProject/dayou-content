# 协作规则 / Contributing

> **核心原则：只有 Lexa（创始人）能提交到 main 分支。**

这条规则适用于 Dayou 项目下的所有仓库：
- [mysterious](https://github.com/AlyciaBHZ/mysterious)（产品主仓库）
- [animal-dayou](https://github.com/AlyciaBHZ/animal-dayou)（宠物命理副产品）
- [dayou-content](https://github.com/AlyciaBHZ/dayou-content)（内容运营与团队协作）

---

## 为什么不允许直接 push 到 main

| 原因 | 说明 |
|------|------|
| **部署一致性** | mysterious 和 animal-dayou 接 Vercel 自动部署，main 任何提交都会立即上线 |
| **部署门禁** | Vercel 要求 commit 作者邮箱是 GitHub 验证邮箱，否则部署失败 |
| **代码审查** | 任何人改产品代码前都需要 Lexa 看一眼，避免破坏现有功能 |
| **责任归属** | 出问题时能清楚追踪是谁的改动 |

---

## 团队成员工作流（按角色）

### 知识库负责人

**你应该做的：**
- ✅ 在 GitHub 网页上提交 Issue（Content Idea Submission）
- ✅ 在 Issue 评论区给脚本反馈（通过 / 需改 / 拒绝）
- ✅ 写每周 Weekly Report Issue
- ✅ 微信和 Lexa 同步紧急情况

**你不应该做的：**
- ❌ 不要 clone 任何 repo 到本地
- ❌ 不要尝试 push 任何分支
- ❌ 不要装 git / Python / Node 这些工具

**理由：你的工作完全在 GitHub 网页上完成。你不需要碰代码。**

### 宣发负责人

**你应该做的：**
- ✅ 在 GitHub 网页上看本周脚本（`workspace/scripts/`）
- ✅ 提交 Weekly Report Issue
- ✅ 在 TikTok / Instagram / Reddit 后台执行发布
- ✅ 微信和 Lexa 同步紧急情况

**你不应该做的：**
- ❌ 不要 clone 任何 repo 到本地
- ❌ 不要直接修改 `team.yaml` 或任何配置文件
- ❌ 不要 push 任何东西到 GitHub

**理由：你的工作场景是平台后台 + GitHub Issue 评论区，不是 git 工作流。**

### 未来加入的技术开发者（如果有）

**如果你是技术开发者，需要改代码：**

1. ✅ Clone 仓库
2. ✅ 创建新分支：`git checkout -b feature/your-task`
3. ✅ 改代码、commit 到自己的分支
4. ✅ Push 分支到 origin：`git push origin feature/your-task`
5. ✅ 在 GitHub 上开 Pull Request，目标分支选 `main`
6. ✅ 等 Lexa review 并合并

**绝对不要：**
- ❌ 直接 push 到 main 分支
- ❌ 强制推送（`git push --force`）任何分支
- ❌ 跳过 PR review 直接 merge
- ❌ 改 git config 让自己的邮箱不在 GitHub 验证列表里

---

## 如果你不小心 push 到了 main

立即通知 Lexa（微信）。**不要尝试自己回滚。** 强制回滚会破坏 Vercel 部署历史。

Lexa 会评估影响并决定是回滚还是 forward fix。

---

## 配置要求（如果你确实需要本地 git）

如果有一天你被授权直接改代码：

```bash
# 必须用 GitHub 验证过的邮箱
# 找到自己的 noreply 邮箱：https://github.com/settings/emails
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
| 不小心改了不该改的东西 | 微信 Lexa（不要自己尝试 fix） |
| 一般问题 | GitHub Issue |

---

## 总结一句话

**Lexa 是 main 分支的唯一守门人。所有改动通过 PR 进 main，由 Lexa merge。团队成员的工作不需要碰 git。**
