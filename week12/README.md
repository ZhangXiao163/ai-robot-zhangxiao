- 1  pip install pybullet numpy # 安装PyBullet
- 2  验证 python3 -c "import pybullet as p; print('PyBullet已安装')"
- 3  拷贝代码 https://course.a-real.me/content/week13.html 13.6.2 Trot步态实现 test.py
- 4  运行代码 python3 test.py  现在狗子可以站起来但现在不能走还会倒下 
- 5  修改代码 让狗子站好并且走起来 
      1. 自动筛选电机关节
      通过遍历模型的所有关节，过滤掉固定件，只保留可旋转的驱动电机。
      for i in range(p.getNumJoints(robot_id)):
          info = p.getJointInfo(robot_id, i)
          joint_type = info[2]
           # 仅保留可旋转的关节 (JOINT_REVOLUTE)
         if joint_type == p.JOINT_REVOLUTE:
          self.joints.append(i)
       2.  绑定四条腿的序号
         明确每条腿对应的物理关节 ID，顺序严格按照：[侧摆, 大腿前摆, 小腿屈伸]。    
       3. 生成对角步态轨迹利用正弦波让对角线的两条腿同步动作，而两组对角腿之间恰好相差 $\pi$（180 度）的相位，形成交替小跑。
             # FR(右前)和RL(左后)同相，FL(左前)和RR(右后)反相
              if leg_name in ["FR", "RL"]:
             swing = amplitude * np.sin(phase)
            else:
              swing = amplitude * np.sin(phase + np.pi)

             # 映射到大腿和小腿关节（大腿往前摆时，小腿反向折叠实现提腿）
             upper_angle = 0.6 + swing
            lower_angle = -1.2 - swing
      4. 机身姿态闭环修正
           通过“倒立摆”式的负反馈逻辑，机身向哪边倾斜，就往反方向加一个补偿量，把身体“顶”回来。
           # 获取机身欧拉角 (Roll 横滚, Pitch 俯仰)
            roll, pitch, _ = p.getEulerFromQuaternion(orientation)

            # P（比例）控制反馈，系数 -0.8 起到恢复力矩的作用
            roll_correction = -0.8 * roll
            pitch_correction = -0.8 * pitch
       5. 展平数据并下发指令
          把 4 条腿算好的角度（叠加了平衡补偿）拼成一个 12 维的长列表，一次性打包发送给所有电机，然后推进仿真。     
          # 叠加平衡补偿
            angles[0] += roll_c   # 侧摆轴改 Roll
            angles[1] += pitch_c  # 前摆轴改 Pitch

            # 一次性阵列化下发控制指令
            p.setJointMotorControlArray(
            bodyIndex=self.robot,
            jointIndices=self.joints,
            controlMode=p.POSITION_CONTROL,
            targetPositions=all_targets # 包含12个角度的列表
                )
            p.stepSimulation() # 物理引擎推进一步

- 6 运行效果  效果图 <br>
      ![这是效果图](readmeimg.png )<br>
      ![[radio.mp4]]


