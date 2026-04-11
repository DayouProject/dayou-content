# Dayou Collaboration Runbook

这是 Dayou 当前统一的协作运行手册，不再按“内容团队固定岗位”来写。

## 先做什么

1. 配好 `Claude / Cursor / Codex` 之一
2. 打开 `https://dayouproject.github.io/dayou-content/`
3. 把首页链接交给你的 agent
4. 让它先带你完成 `gh auth`
5. 让它再带你 clone 三个仓库：
   - `DayouProject/mysterious`
   - `DayouProject/animal-dayou`
   - `DayouProject/dayou-content`

## clone 后怎么直接用 `/daily`

在任意一个 Dayou 仓库里：

- Claude Code：输入 `/daily`
- Cursor：输入 `/daily`
- Codex：说 `给我一个今天的 /daily`

agent 必须先：

1. 检查 `gh auth`
2. 确认三个仓库都在本地
3. 读取 `README`、`TODO`（存在时）、open Issues
4. 再输出一屏内中文 daily

## 正式协作怎么留痕

聊天只负责整理，正式留痕一律回 GitHub：

- 需求
- 决策
- office hours 结论
- 实现进度
- 验收结果

## 什么不用做

- 不用自己研究 Node.js / Vercel
- 不用自己想完整 git 工作流
- 非技术协作者不用直接改代码

## 紧急情况

下面这些情况直接找 Lexa：

- 私有仓库 clone 失败
- GitHub 权限不对
- `/daily` 跑不起来
- 误操作了 `git push`
