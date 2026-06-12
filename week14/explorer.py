def p_control_loop(self):
    # 伪代码：自研或优化的巡墙状态机
    if self.front_blocked:
        # 前方有墙，果断左转
        self.msg.linear.x = 0.0
        self.msg.angular.z = 1.5  # 左转速度
    elif self.right_open:
        # 右侧空旷，说明有右拐弯机会，执行向右巡线
        self.msg.linear.x = 1.0
        self.msg.angular.z = -1.0 # 弧度向右靠拢
    else:
        # 右侧有墙且前方无阻挡，安心直行
        self.msg.linear.x = 1.5
        self.msg.angular.z = 0.0
    
    self.publisher_.publish(self.msg)