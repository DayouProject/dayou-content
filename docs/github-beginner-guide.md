# GitHub 零基础入门指南

> 从注册账号到参与 Dayou 内容协作，一步一步教你。
> 预计时间：15 分钟。

---

## 第一步：注册 GitHub 账号

1. 打开 https://github.com/join
2. 填写：
   - **Username（用户名）**：英文，比如你的名字拼音 `zhangsan`
   - **Email（邮箱）**：填你常用的邮箱
   - **Password（密码）**：至少 8 位，包含数字和字母
3. 点击 **Create account**（创建账号）
4. 去邮箱收验证邮件，点击验证链接
5. 完成！你现在有一个 GitHub 账号了

---

## 第二步：接受仓库邀请

项目负责人会邀请你加入 `dayou-content` 仓库。

1. 你的邮箱会收到一封来自 GitHub 的邀请邮件
2. 点击邮件中的 **View invitation**（查看邀请）
3. 点击 **Accept invitation**（接受邀请）
4. 现在你可以访问 https://github.com/AlyciaBHZ/dayou-content

---

## 第三步：熟悉界面

打开 https://github.com/AlyciaBHZ/dayou-content ，你会看到：

```
dayou-content/
├── README.md          ← 项目说明（你正在看的）
├── RUNBOOK.md         ← 你的操作手册（必读！）
├── corpus/            ← 古典文本素材
├── workspace/         ← 生成的脚本和视频
└── ...
```

**重要按钮位置：**
- **Issues**（问题/任务）：在页面顶部的标签栏，点这里提交内容概念和周报
- **Code**（代码）：查看文件内容
- **Pull requests**：暂时不需要用

---

## 第四步：提交内容概念（你的核心工作）

这是你每周一要做的事情。

### 操作步骤：

1. 点击页面顶部的 **Issues** 标签
2. 点击绿色按钮 **New issue**（新建问题）
3. 选择模板 **Content Idea Submission / 内容灵感提交**
4. 按模板填写：

```
## Source Text / 经典来源
易经

## Concept 1 / 概念一
Core idea: 乾卦"潜龙勿用"——时机未到时蛰伏积蓄的智慧
Modern angle: 当你刚到一个新环境（新工作、新城市），不要急于表现，先观察
Target emotion: calm（平静）

## Concept 2 / 概念二
Core idea: 五行相生——水生木，滋养才能成长
Modern angle: 人际关系中，支持比竞争更能带来成长
Target emotion: reflective（反思）
```

5. 点击 **Submit new issue**（提交）
6. 完成！项目负责人会看到你的概念并生成脚本

---

## 第五步：审核生成的脚本

脚本生成后，你需要检查内容是否准确。

### 怎么找到脚本：

1. 在仓库首页，点击 `workspace` 文件夹
2. 点击 `scripts` 文件夹
3. 找到本周的文件夹（比如 `2026-W16`）
4. 点击 `scripts` 子文件夹
5. 你会看到 7 个 `.md` 文件，每个是一天的视频脚本

### 怎么看脚本：

点击任意一个 `.md` 文件，GitHub 会自动渲染成易读的格式：

```
## HOOK
If life feels unclear right now, this ancient line is telling you where to look.

## BODY
1. This line points to what to do when life feels uncertain...
2. The message is simple: stop trying to control every outcome...
3. Use the teaching as a mirror for your next decision...

## CTA
Follow Dayou for one grounded piece of Eastern wisdom every day.
```

### 怎么给反馈：

1. 回到你提交的那个 Issue（Issues 标签 → 找到你的 Issue）
2. 在下方评论区写反馈，比如：
   - "脚本 03 太抽象了，加一个具体的例子"
   - "脚本 05 的 CTA 改成提到'五行属性'"
   - "脚本 01 很好，通过"
3. 点击 **Comment**（评论）

---

## 第六步：提交周报

每周日，记录本周的内容表现。

1. **Issues** → **New issue** → 选择 **Weekly Report / 周报**
2. 填写本周数据：

```
## Published This Week / 本周发布
- Videos published: 7/7
- Platform: TikTok

## Performance / 数据表现
| Day | Title | Views | Likes | Comments |
|-----|-------|-------|-------|----------|
| Mon | What to do when life feels uncertain | 1,234 | 45 | 12 |
| Tue | How to stop forcing timing | 890 | 32 | 8 |
...
```

3. 数据从哪来？打开 TikTok Creator 后台，复制每条视频的数据
4. 提交 Issue

---

## 常见问题

### Q: 我不小心改了什么东西怎么办？
**A:** 不用担心。你在 GitHub 网页上浏览文件是只读的，不会改到任何东西。只有 Issues（评论区）是你可以写入的地方。

### Q: 我能看到其他人提交的概念吗？
**A:** 可以。点击 Issues 标签就能看到所有人提交的概念和周报。

### Q: 怎么编辑我已经提交的 Issue？
**A:** 打开你的 Issue，点击右上角的三个点 `...`，选择 **Edit**（编辑）。

### Q: 我提交了概念但没人回应怎么办？
**A:** 微信联系项目负责人。GitHub Issue 是异步工具，紧急事情直接微信。

### Q: 我可以用手机操作吗？
**A:** 可以。GitHub 网页在手机浏览器上可以正常使用。也可以下载 GitHub 手机 App。

### Q: 我需要学 git 命令吗？
**A:** 不需要。你的所有操作都在 GitHub 网页上完成（提交概念、审核脚本、写周报）。只有项目负责人需要用命令行。

---

## 术语表

| 看到的英文 | 意思 |
|-----------|------|
| Repository / Repo | 仓库，就是我们的项目文件夹 |
| Issue | 问题/任务，我们用它来提交概念和周报 |
| Comment | 评论，在 Issue 下方写反馈 |
| Code | 代码/文件，点这里查看项目文件 |
| Commit | 提交，指负责人保存了一次代码修改 |
| Branch | 分支，暂时不需要了解 |
| Pull Request (PR) | 合并请求，暂时不需要了解 |
| Markdown (.md) | 一种文本格式，GitHub 会自动渲染成易读的样子 |

---

## 下一步

1. 注册完 GitHub 后，把你的用户名发给项目负责人
2. 等待邀请邮件，接受邀请
3. 阅读 [RUNBOOK.md](../RUNBOOK.md)，了解你的每周工作流程
4. 每周一提交内容概念，每周日提交周报
5. 有问题随时在 Issue 里提问或微信联系负责人
