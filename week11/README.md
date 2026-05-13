1 docker run -p 6080:80 --security-opt seccomp=unconfined --shm-size=512m -v C:\zhangxiao\robot:/home/ws ghcr.io/tiryoh/ros2-desktop-vnc:humble
//绑定一个镜像文件目录到虚拟机 docker 执行成功之后 会把两个目录镜像 修改一个另一个也会修改
2 在ubantu里 安装opencv
   pip install opencv-python opencv-contrib-python 
3  docker ps 查看当前状态 
4    docker commit f900c54894b1 ros2-zhangxiao-work:v1  提交自己的版本
5 docker images 查看提交后的状态
6 杀掉之前启动的ros 重新连接自己的提交镜像 
   docker run   -p 6080:80 --name my_ros_container  ros2-zhangxiao-work:v1

     ![这是效果图](commit.png )<br>
