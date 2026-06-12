# 🤖 AI 机器人课程实践仓库 - AIRobot

<p align="center">
  <img src="https://img.shields.io/badge/ROS2-Humble-blue?style=flat-square&logo=ros" alt="ROS2">
  <img src="https://img.shields.io/badge/Simulation-PyBullet-orange?style=flat-square" alt="PyBullet">
  <img src="https://img.shields.io/badge/Environment-Docker%20%7C%20WSL2-green?style=flat-square&logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
</p>

> 💡 **项目简介**：本仓库记录了在 **Ubuntu / WSL2** 环境下，围绕 **ROS2、PyBullet 仿真平台与 Docker 容器技术**展开的 AI 机器人全栈开发学习历程。核心涵盖机器人底盘控制、四足机器人 Trot 步态算法、以及智能机器人系统所必需的数学与视觉算法基石。

🌐 **在线文档访问**：[👉 点击进入 GitHub Pages 预览](https://zhangxiao163.github.io/ai-robot-zhangxiao/)

---

## 👨‍🎓 学生与学术信息

| 基础项目 | 详细内容 |
| :--- | :--- |
| **姓名 (Name)** | zhangxiao | 张孝 | 장효 |
| **学号 (Student ID)** | 20242032 |
| **项目周期 (Timeline)** | 2026-03-11 ~ 至今 |

---

## 💻 统一开发环境 (Environment)

| 组件/工具 | 技术选型与版本 | 作用说明 |
| :--- | :--- | :--- |
| **操作系统** | Windows 11 + WSL2 / Ubuntu 22.04 LTS | 核心开发与运行环境 |
| **机器人操作系统** | ROS2 Humble Hawksbill | 节点通信与分布式控制框架 |
| **集成开发环境** | VSCode + WSL 远程扩展 | 代码编写、调试与版本控制 |
| **物理仿真平台** | PyBullet Simulation | 四足机器人物理引擎与动力学仿真 |
| **容器与虚拟化** | Docker 🚀 | 保证开发环境跨平台的一致性与快速部署 |
| **远程连接** | Tailscale + Termius | 移动端/异地远程调试及控制 |

---

## 📚 课程目录与核心作业 (Curriculum & Homework)

这里记录了每周的课程要点与实践成果。点击 📂 即可跳转至对应周次的详细作业、代码及推导报告：

### 🛠️ 阶段一：Linux 基础与 ROS2 机器人入门
* **Week 02 - Ubuntu 与 ROS2 环境安装**
  * 安装 Ubuntu 系统、配置 ROS2 Humble 软件源、成功运行 `Turtlesim` 小乌龟。
  * 📂 [查看 Week 02 作业](./week02/README.md) *(注: 对应 week01 目录)*
* **Week 03 - 小乌龟运动控制实践**
  * 深入 ROS2 节点通信，控制小乌龟实现几何画圆与平滑轨迹控制。
  * 📂 [查看 Week 03 作业](./week03/README.md)
* **Week 04 - 机器狗基础控制与几何绘制**
  * 启动、放倒机器狗底盘，编写 ROS2 节点控制小乌龟绘制精准正方形。
  * 📂 [查看 Week 04 作业](./week04/README.md)
* **Week 05 - ROS2 核心运动控制**
  * 进阶控制，编写通用几何轨迹发布器（画圆、画线控制）。
  * 📂 [查看 Week 05 作业](./week05/README.md)
* **Week 06 - 全景监控系统集成**
  * 编译并运行 `ros2_ws` 工作空间项目，打通传感器数据链路实现全景监控。
  * 📂 [查看 Week 06 作业](./week06/README.md)
* **Week 07 - 规范化代码管理**
  * 重构与整理 Git 仓库结构，优化大文件及历史提交记录。
  * 📂 [查看 Week 07 作业](./week07/README.md)

---

### 🧠 阶段二：工业级工程容器化与智能算法基石
* **Week 08 - Docker 机器人环境配置**
  * 编写 Dockerfile，在容器内隔离运行 ROS2 并在宿主机 X11 转发成功显示小乌龟。
  * 📂 [查看 Week 08 作业](./week08/README.md)

* **Week 09 - 智能基石：从线性代数到智能机器人系统**
  * 🪐 本周专注于智能机器人的“数学灵魂”与算法闭环，包含以下核心模块：
    1. **线性代数底层**：坐标空间变换、旋转矩阵、四元数、特征值与 SVD 分解。
    2. **机器人运动学**：DH 参数法、正运动学（FK）与逆运动学（IK）雅可比矩阵迭代求解。
    3. **计算机视觉数学**：针孔相机模型、内外参矩阵、对极几何与双目三维重建。
    4. **路径规划算法**：基于图搜索的 $A^*$ 算法、基于随机采样的 RRT/RRT* 与局部避障。
  * 📂 [查看 Week 09 算法专题作业](./week09/README.md)

* **Week 010 - 虚拟机目录挂载优化**
  * 绑定镜像文件目录，配置高级虚拟机共享文件目录，优化资源传输效率。
  * 📂 [查看 Week 10 作业](./week10/README.md)
* **Week 11 - 开发环境系统镜像提交**
  * 打包当前配置完整的 Ubuntu 运行环境，提交并发布一键部署镜像。
  * 📂 [查看 Week 11 作业](./week11/README.md)

---

### 🐕 阶段三：四足仿生机器人控制与远程运维
* **Week 12 - PyBullet 四足机器人 Trot 步态实现**
  * 建立四足机器人物理模型，编写基于 VMC（虚拟模型控制）或静力学的**小跑步态（Trot Gait）**算法。
  * 实现机器狗在复杂地形下的姿态平衡控制与高稳定性行走。
  * 📂 [查看 Week 12 步态作业](./week12/README.md)
* **Week 13 - Tailscale 虚拟局域网与 WSL 远程连接**
  * 在 WSL 中部署 Tailscale 节点，打破内网限制。
  * 使用手机端 Termius 远程 SSH 连接 WSL 终端，实现随时随地远程调参和运行程序。
  * 📂 [查看 Week 13 作业](./week13/README.md)
* **Week 14 - 实现一个支持手机远程控制和自主探索迷宫的小乌龟机器人系统。
  * 通过手机浏览器访问控制网页；。
  * 基于经典巡墙算法（Wall Following）自主探索迷宫的小乌龟机器人。
  * 📂 [查看 Week 14 作业](./week14/README.md)
---

## 🛠️ 技术栈总览 (Tech Stack)

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 🚀 机器人开发:  ROS2 (Humble) / Gazebo / PyBullet (物理仿真)           │
├────────────────────────────────────────────────────────────────────────┤
│ 💻 基础设施:    Ubuntu 22.04 / WSL2 / Docker (容器化) / Tailscale       │
├────────────────────────────────────────────────────────────────────────┤
│ 🔢 核心算法:    运动学 (FK/IK) / Trot步态 / 线性代数视觉几何 / A*, RRT  │
├────────────────────────────────────────────────────────────────────────┤
│ 🐍 编程语言:    Python / C++ / Bash Shell                              │
└────────────────────────────────────────────────────────────────────────┘