## week6 运行ros2_ws 项目 并且实现全景监控
-  1 new folder ros2_ws and    git clone https://github.com/ai-robot-class/ros2_kitti_publishers.git  <br>
    新建文件夹ros2_ws 克隆git 项目 <br>
- 2 download  imagedata  https://drive.google.com/file/d/1lCOOkoUp1RRrFhUwRVNVwRWIclv-etBu/view?usp=drive_link<br>
  下载资源图片文件<br>
- 3 copy data to \\wsl.localhost\Ubuntu-22.04\home\zhangxiao\ros2_ws\data    <br>
- 4 build and run    //编译并且执行下面的命令<br>
   cd ~/ros2_ws<br>
   colcon build --cmake-clean-cache<br>
   source ./install/setup.bash<br>
   ros2 run ros2_kitti_publishers kitti_publishers<br>
- 5 open another terminal run   //打开一个新的窗口运行 新的命令<br>
   ros2 daemon start<br>
   rviz2  <br>
- 6 set cofig   on the window    //在运行出的界面上设置config<br>
    file/openConfig  "\\wsl.localhost\Ubuntu-22.04\home\zhangxiao\ros2_ws\src\ros2_kitti_publishers\default.rviz" <br>
     save <br>
       ![这是效果图](img2.png) <br>
- 7 back first terminal run     //返回第一个窗口运行命令<br>
  ros2 run ros2_kitti_publishers kitti_publishers<br>
  ![这是效果图](img1.png) <br>
 


