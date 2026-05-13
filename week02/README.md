## 运行小乌龟程序并且画圈画圆

- 1 chorome download  vscode https://code.visualstudio.com/ and install <br>
  浏览器下载 vscode 并且安装 <br>
- 2  download WSL and run ubuntu <br>
   下载WSL 并且运行上节课的乌班图 <br> 
- 3 open ubuntu root and create own dictory my is  /robot  <br>
  打开乌班图根目录 创建自己的目录         /robot   <br>
- 4  create ssh secret and clone git  repository <br>
   创建ssh 密钥并且克隆远程仓库到虚拟机 <br>
   https://zhuanlan.zhihu.com/p/688103044<br>
- 5  learn ros order <br>
   学习 ros 命令 <br>
- 6  example  举例<br>
  ORDER1:  ros2 run turtlesim turtlesim_node  <br>
    //run turtle  运行小乌龟 <br>
  open anther window  打开另外一个窗口 <br>

  ORDER2:  ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"<br>
    //小乌龟画圈 见效果图 <br>
     ![这是效果图](小乌龟画圈.png )<br>
  //run turtle as line see in picture  让小乌龟按线性前进 效果见截图  ![这是效果图](小乌龟运动.png )<br>
  ORDER3: ros2 topic echo /turtle1/pose    <br>
  //listen turtle postion  see in picture <br>
   监听小乌龟坐标 效果见截图    ![这是效果图](监听小乌龟位置.png )
         


