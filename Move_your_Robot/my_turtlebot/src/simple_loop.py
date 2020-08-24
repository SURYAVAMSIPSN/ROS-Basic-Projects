#! /usr/bin/env python

import rospy

rospy.init_node("McFries")

rate = rospy.Rate(2)
while not rospy.is_shutdown(): # while not Ctrl + C
    print("I need your help, McFries.")
    rate.sleep()