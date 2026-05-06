- 1 docker run -p 6080:80 --security-opt seccomp=unconfined --shm-size=512m -v C:\zhangxiao\robot:/home/ws ghcr.io/tiryoh/ros2-desktop-vnc:humble
     //绑定一个镜像文件目录到虚拟机 docker 执行成功之后 会把两个目录镜像 修改一个另一个也会修改
- 2    安装opencv 
      pip install opencv-python opencv-contrib-python //先安装环境
- 3
       把代码copy到 test.py文件里 下载cat.png 放到同一目录下 执行 python test.py 
- 4        效果图 <br>
     ![这是效果图](garyCat.png )<br>
     