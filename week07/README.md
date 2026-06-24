# 🚀 Week 7 项目展示与仓库整理

欢迎来到第七周的项目仓库！本项目主要用于展示本周的开发成果，并已通过 GitHub Pages 成功部署。

* **🎯 本周任务：** 规范化目录管理、完善 README 效果展示、配置 GitHub Pages 部署。

---

## 📂 目录结构

```text
├── week1/                 # 第一周项目
├── week2/                 # 第二周项目
│   └── ...
├── week7/                 # 第七周项目文件夹
│   ├── images/            # 效果图文件夹
│   │   └── result.png     # 页面效果图
│   ├── index.html         # 网页主入口
│   └── README.md          # 本周项目说明（内含效果图）
└── README.md              # 根目录总说明（当前文件）


🛠 GitHub Pages 链接生成步骤
要在仓库的 Settings 中生成个人在线预览链接，请按照以下步骤操作：

进入设置： 点击你 GitHub 仓库右上角的 Settings（齿轮图标）。

找到 Pages： 在左侧导航栏中，向下滚动找到 Code and automation 栏目，点击 Pages。

配置分支（Build and deployment）：

Source 保持默认的 Deploy from a branch。

Branch 下拉菜单将 None 改为 main（或 master）。

目录选择 /root（如果你的主入口 index.html 在根目录）。

保存配置： 点击右侧的 Save 按钮。

获取链接： 稍等 1 分钟左右刷新页面，顶部会出现一行绿色的提示：“Your site is live at ...”，那个 URL 就是你的个人动态链接。

📝 Markdown 常用语法速查
1. 标题
使用 # 号标记，支持一到六级标题。

Markdown
# 一级标题
## 二级标题
### 三级标题
2. 文本样式
Markdown
**这是加粗文本**
*这是斜体文本*
~~这是删除线~~
`单行行内代码`
3. 列表
Markdown
- 无序列表项 A
- 无序列表项 B

1. 有序列表项一
2. 有序列表项二
4. 链接与图片
Markdown
[点击跳转的文字](https://www.example.com)
![图片说明](图片相对路径或网络地址)
5. 代码块
使用三个反引号包裹，并可以指定语言（如 html, css, javascript）：

JavaScript
console.log("Hello, GitHub Pages!");
