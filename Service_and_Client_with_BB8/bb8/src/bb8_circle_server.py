#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist
def my_callback(request):
    
    move = Twist()
    move.linear.x = 0.5
    move.angular.z = 0.5
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    pub.publish(move)
    return EmptyResponse()

rospy.init_node("bb8_server")
service = rospy.Service("/move_bb8_in_circle", Empty, my_callback)
rospy.spin()
