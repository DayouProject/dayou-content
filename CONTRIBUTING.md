# 协作规则 / Contributing

> **核心原则：只有 Lexa 能 merge 到 `main`。**
>
> **团队成员 clone 仓库到本地，是为了完成 `gh auth`、跑 repo-native `/daily`、读上下文和走 Issue 协作，不是为了直接 push `main`。**

这条规则适用于 Dayou 项目下的三个仓库：
- [mysterious](https://github.com/DayouProject/mysterious)
- [animal-dayou](https://github.com/DayouProject/animal-dayou)
- [dayou-content](https://github.com/DayouProject/dayou-content)

---

## 最小本地流程

### 第一次设置

1. 先配好 `Claude / Cursor / Codex` 之一
2. 先完成 `gh auth`
3. 先把三个仓库 clone 到同一个父目录下

```bash
gh auth status
gh auth login
gh repo clone DayouProject/mysterious
gh repo clone DayouProject/animal-dayou
gh repo clone DayouProject/dayou-content
```

### clone 后怎么直接用 `/daily`

在任意一个 Dayou 仓库里：

- Claude Code：直接输入 `/daily`
- Cursor：直接输入 `/daily`
- Codex：直接说 `给我一个今天的 /daily`

repo 内的 agent 应该先做四件事：

1. 确认 `gh auth` 已完成
2. 确认三个仓库都已经在本地
3. 读取三个仓库的 `README`、`TODO`（存在时）、open Issues
4. 再输出一屏内的中文 daily

daily 的标准输出结构：

```text
今天关注的仓库：
昨天：
今天：
Blockers：
需要确认：
```

---

## 非技术协作者

你的默认产出不通过 `git push`，而是通过 GitHub Issues：

- 提需求
- 留现场反馈
- 补上下文
- 记录 office hours 结论
- 跟踪验收结果

默认不要直接改代码，不要直接 push 任意分支。

---

## 技术开发者

如果你需要改代码：

1. 从 `main` 拉最新
2. 新建功能分支
3. 在功能分支上开发
4. 开 Pull Request
5. 由 Lexa review / merge

绝对不要：

- `git push origin main`
- `git push --force` 到共享分支
- 跳过 PR 直接合并

### Git 邮箱配置

```bash
git config --global user.email "你的 GitHub 验证邮箱"
git config --global user.name "你的 GitHub 用户名"
```

否则 Vercel 侧会直接拦部署。

---

## 紧急情况

下面这些情况直接找 Lexa：

- `gh auth` 卡住
- 私有仓库 clone 不下来
- `/daily` 跑不起来
- 误操作了 `git push`
- 仓库权限不对

---

## 一句话总结

**先配 AI，先做 `gh auth`，先 clone 三个仓库，再用 repo-native `/daily` 对齐今天要做什么。正式结论一律回 GitHub。**
