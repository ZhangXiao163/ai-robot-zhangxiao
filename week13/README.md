# Week 14 - Tailscale + WSL 远程连接配置教程

## 1. 在 WSL 中安装 Tailscale

在 WSL 终端执行以下命令：

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo service tailscaled start
sudo tailscale up
```

执行 `sudo tailscale up` 后，会输出一个登录链接，例如：

```text
https://login.tailscale.com/a/10815ad1015c20
```

在浏览器中打开该链接并完成登录授权。

---

## 2. 手机安装 Tailscale

在手机上下载安装 Tailscale，并确保：

- 手机与 WSL 使用 **同一个 Tailscale 账户登录**
- 登录成功后，设备会自动加入同一个私有网络

### 效果图

![Tailscale 连接效果](wsl2.png)

---

## 3. 查看当前网络状态

在 WSL 中执行：

```bash
tailscale status
tailscale ip -4
```

说明：

- `tailscale status`：查看当前设备连接状态
- `tailscale ip -4`：查看当前 Tailscale IPv4 地址

---

## 4. 手机安装 Termius

在手机应用商店下载安装：

- **Termius**

用于后续通过 SSH 远程连接 WSL。

---

## 5. 在 WSL 中安装 SSH 服务

执行以下命令：

```bash
sudo apt update
sudo apt install openssh-server -y
sudo service ssh start
```

然后查看当前 Tailscale IP：

```bash
tailscale ip -4
```

示例输出：

```text
100.85.174.99
```

---

## 6. 使用手机 Termius 连接 WSL

在 Termius 中新建 SSH 连接：

| 配置项 | 内容 |
|---|---|
| Host | `100.85.174.99` |
| Username | Ubuntu 用户名 |
| Password | Ubuntu 用户密码 |

连接成功后，即可通过手机远程访问 WSL。

### 效果图

![SSH 连接效果](wsl1.png)

---

# 效果

完成后，你可以：

- 在手机上远程访问 WSL
- 使用 SSH 管理 Linux 环境
- 在任何网络环境下安全连接自己的开发环境
- 不需要公网 IP 或端口映射

---
## 7. 安装sudo apt update     sudo apt install python3-pip -y   
     pip3 install -r  requirements.txt
     python3 camera_bridge.py 


---
## 8.在手机浏览器中打开：

https://100.85.174.99:5000     

![连接效果](result.jpg)