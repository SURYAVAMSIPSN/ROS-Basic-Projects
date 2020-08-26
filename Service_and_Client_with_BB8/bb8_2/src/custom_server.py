#! /usr/bin/env python

import rospy
from bb8_2.srv import CustomServiceMessage, CustomServiceMessageResponse
from geometry_msgs.msg import Twist

def callback(request):
    response = CustomServiceMessageResponse()
    global count 
    response.status = False
    while count < request.duration:
        move.linear.x = 0.5
        move.angular.z = 0.5
        pub.publish(move)
        rate.sleep()
        count += 1
    response.status = True
    move.linear.x = 0 
    move.angular.z = 0
    pub.publish(move)
    return response

move = Twist()
count = 0
rospy.init_node("bb8_2_server")
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
service = rospy.Service('/move_bb8_in_circle_custom', CustomServiceMessage, callback)
rate = rospy.Rate(2)
rospy.spin()
