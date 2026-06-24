# Week 07 - 仓库整理与 GitHub Pages 部署

本周对课程仓库进行结构整理，完善 README 展示方式，并配置 GitHub Pages 作为在线文档入口。

## 本周目标

- 规范课程作业目录结构。
- 整理每周 README 与素材文件。
- 学习 GitHub Pages 的部署流程。
- 让项目成果可以通过网页链接预览。

## 本周工作内容

### 1. 仓库结构整理

将每周作业按照 `weekXX/` 的方式存放，便于查找、提交和展示：

```text
ai-robot-zhangxiao/
├── readme.md
├── week02/
├── week03/
├── week04/
├── week05/
├── week06/
├── week07/
└── ...
```

### 2. README 展示优化

README 不只记录命令，也需要说明：

- 本周任务目标。
- 关键文件作用。
- 实验运行步骤。
- 结果截图或视频。
- 学习总结。

这样的结构更适合课程作业检查，也方便自己复盘。

### 3. GitHub Pages 配置

在 GitHub 仓库中进入：

```text
Settings -> Pages -> Build and deployment
```

选择部署分支后，GitHub 会生成在线预览链接。根目录 README 和各周 README 可以作为课程成果展示入口。

## 常用 Git 操作

查看当前状态：

```bash
git status
```

添加文件：

```bash
git add .
```

提交修改：

```bash
git commit -m "update weekly readme"
```

推送到远程仓库：

```bash
git push
```

## 学习总结

本周重点不是新增机器人算法，而是提升项目工程化管理能力。规范的目录、清晰的 README 和在线展示页面，可以让整个课程项目更完整、更容易被阅读和维护。
