# AI 机器人课程实践仓库 - AIRobot

本仓库用于记录 AI 机器人课程的阶段性实践成果。项目围绕 ROS2、turtlesim、PyBullet、Docker、WSL2 与远程运维工具展开，涵盖机器人基础控制、仿真环境搭建、运动算法、路径规划、四足机器人步态以及手机远程控制等内容。

在线文档预览：[GitHub Pages](https://zhangxiao163.github.io/ai-robot-zhangxiao/)

---

## 项目信息

| 项目 | 内容 |
| :--- | :--- |
| 姓名 | zhangxiao / 张孝 / 장효 |
| 学号 | 20242032 |
| 项目周期 | 2026-03-11 至今 |
| 课程方向 | AI 机器人系统开发与实践 |

---

## 项目目标

本项目的目标是通过连续课程实践，逐步建立完整的机器人开发能力：

- 熟悉 Ubuntu、WSL2、Docker 等机器人开发环境。
- 掌握 ROS2 节点、话题、消息发布与订阅等核心机制。
- 使用 turtlesim 完成基础运动控制与路径绘制。
- 使用 PyBullet 搭建机器人仿真与四足机器人步态实验。
- 理解线性代数、运动学、视觉几何、路径规划等智能机器人基础算法。
- 实现基于手机浏览器的远程控制与自主探索机器人系统。

---

## 开发环境

| 组件 | 技术选型 | 说明 |
| :--- | :--- | :--- |
| 操作系统 | Windows 11 + WSL2 / Ubuntu 22.04 LTS | 主要开发与运行环境 |
| 机器人系统 | ROS2 Humble Hawksbill | 节点通信、话题发布、机器人控制 |
| 开发工具 | VSCode + WSL 远程扩展 | 代码编写、调试与版本管理 |
| 仿真平台 | turtlesim / PyBullet | 小乌龟控制与四足机器人仿真 |
| 容器工具 | Docker | 环境隔离与可复现部署 |
| 远程连接 | Tailscale / Termius | 手机端与异地远程调试 |
| 编程语言 | Python / C++ / Bash | ROS2 节点、脚本与自动化工具 |

---

## 仓库结构

```text
ai-robot-zhangxiao/
├── readme.md
├── week02/    # Ubuntu 与 ROS2 环境安装
├── week03/    # turtlesim 基础运动控制
├── week04/    # 机器人基础控制与几何绘制
├── week05/    # ROS2 轨迹发布与运动控制
├── week06/    # 全景监控系统集成
├── week07/    # Git 仓库整理与规范化
├── week08/    # Docker 机器人环境配置
├── week09/    # 智能机器人数学与算法基础
├── week10/    # 虚拟机目录挂载优化
├── week11/    # 开发环境镜像提交
├── week12/    # PyBullet 四足机器人 Trot 步态
├── week13/    # Tailscale 与 WSL 远程连接
└── week14/    # 手机遥控与自主探索小乌龟系统
```

---

## 课程实践目录

### 阶段一：Linux 基础与 ROS2 入门

| 周次 | 主题 | 主要成果 |
| :--- | :--- | :--- |
| [Week 02](./week02/README.md) | Ubuntu 与 ROS2 环境安装 | 安装 Ubuntu 与 ROS2 Humble，运行 turtlesim 示例。 |
| [Week 03](./week03/README.md) | 小乌龟运动控制实践 | 理解 ROS2 节点通信，控制 turtlesim 完成基础运动。 |
| [Week 04](./week04/README.md) | 机器人基础控制与几何绘制 | 编写 ROS2 控制节点，完成正方形等几何轨迹绘制。 |
| [Week 05](./week05/README.md) | ROS2 核心运动控制 | 编写通用轨迹发布器，实现画圆、画线等控制任务。 |
| [Week 06](./week06/README.md) | 全景监控系统集成 | 编译并运行 ROS2 工作空间，完成传感器数据链路集成。 |
| [Week 07](./week07/README.md) | 规范化代码管理 | 整理 Git 仓库结构，优化文件组织与提交记录。 |

### 阶段二：容器化环境与智能算法基础

| 周次 | 主题 | 主要成果 |
| :--- | :--- | :--- |
| [Week 08](./week08/README.md) | Docker 机器人环境配置 | 编写 Dockerfile，在容器中运行 ROS2 与 turtlesim。 |
| [Week 09](./week09/README.md) | 智能机器人数学基础 | 学习线性代数、运动学、视觉几何、A* 与 RRT 等算法。 |
| [Week 10](./week10/README.md) | 虚拟机目录挂载优化 | 配置共享目录与镜像文件挂载，提高开发效率。 |
| [Week 11](./week11/README.md) | 开发环境镜像提交 | 打包完整 Ubuntu/ROS2 开发环境，支持快速复现。 |

### 阶段三：四足仿真、远程运维与综合项目

| 周次 | 主题 | 主要成果 |
| :--- | :--- | :--- |
| [Week 12](./week12/README.md) | PyBullet 四足机器人 Trot 步态 | 搭建四足机器人仿真模型，实现小跑步态控制。 |
| [Week 13](./week13/README.md) | Tailscale 与 WSL 远程连接 | 使用 Tailscale 打通虚拟局域网，并通过手机远程连接 WSL。 |
| [Week 14](./week14/README.md) | 手机遥控与自主探索小乌龟系统 | 实现手机网页遥控、ROS2 桥接通信与右手法则巡墙探索。 |

---

## Week 14 综合项目亮点

第十四周项目是本仓库的综合实践内容，目标是实现一个支持手机远程控制和自主探索迷宫的小乌龟机器人系统。

核心模块包括：

- 手机端网页控制界面：通过浏览器发送前进、后退、左转、右转等指令。
- Python Bridge Server：接收网页请求并转换为 ROS2 控制消息。
- ROS2 控制节点：向 `/turtle1/cmd_vel` 发布 `Twist` 消息，驱动 turtlesim 运动。
- 自主探索算法：基于 Wall Following 与 Right-Hand Rule，实现迷宫巡墙探索。

系统流程：

```text
手机浏览器
    ↓
网页控制界面
    ↓
HTTP / WebSocket
    ↓
Python Bridge Server
    ↓
ROS2 Node
    ↓
/turtle1/cmd_vel
    ↓
turtlesim
```

效果截图见：[week14/img1.png](./week14/img1.png)

---

## 技术栈概览

| 分类 | 技术 |
| :--- | :--- |
| 机器人开发 | ROS2 Humble, turtlesim, PyBullet |
| 仿真与控制 | Twist 消息, ROS2 Topic, Wall Following, Right-Hand Rule, Trot Gait |
| 工程环境 | Ubuntu 22.04, WSL2, Docker, VSCode |
| 远程运维 | Tailscale, Termius, SSH |
| 算法基础 | FK/IK, Jacobian, A*, RRT/RRT*, 视觉几何 |
| 编程语言 | Python, C++, Bash |

---

## 运行建议

不同周次的作业依赖环境不同，建议进入对应目录阅读该周 README 后再运行。

通用 ROS2 环境初始化示例：

```bash
source /opt/ros/humble/setup.bash
```

运行 turtlesim 示例：

```bash
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key
```

若运行自定义 ROS2 工作空间，通常需要先编译并加载环境：

```bash
colcon build
source install/setup.bash
```

---

## 学习总结

通过本项目的持续实践，逐步完成了从基础环境搭建到综合机器人系统开发的学习闭环。项目不仅覆盖 ROS2 通信机制和机器人运动控制，也延伸到了容器化部署、远程连接、仿真平台、路径搜索和自主探索算法等内容，为后续真实机器人平台开发打下基础。
