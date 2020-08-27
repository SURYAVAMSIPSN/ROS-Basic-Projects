#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class BB8:
    def __init__(self):
        self.cmd = Twist()
        self.publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.rate = rospy.Rate(1)

    def move_robot(self, linear_vel=0.2, angular_vel=0.2):
        self.cmd.linear.x = linear_vel
        self.cmd.angular.z = angular_vel
        rospy.loginfo("Moving BB8")
        self.publisher.publish(self.cmd)
        
    def halt(self):
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        rospy.loginfo("Stopped.")
        self.publisher.publish(self.cmd)
    
    def move_with_time(self, time, lin, ang):
        count = 0
        while count <= time:
            self.move_robot(lin, ang)
            count += 1
            self.rate.sleep()
        
        self.halt()

if __name__ == '__main__':
    rospy.init_node('move_bb8_test', anonymous=True)
    movebb8_object = BB8()
    try:
        movebb8_object.move_with_time()
    except rospy.ROSInterruptException:
        pass
        
        
    

