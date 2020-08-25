#! /usr/bin/env python 

# Obstacle avoidance using topics, pubs, subs and messages

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



rospy.init_node("topics_quiz_node")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

t = Twist()
t.linear.x = 0.2
t.angular.z = 0.0

rate = rospy.Rate(2)

def callback(msg):
    global t
    ranges = msg.ranges
    l = len(ranges)
    
    # l split into 0, 0.25, 0.5, 0.75, 1
    middle = ranges[int(0.5 * l)]

    left = [ranges[0], ranges[int(0.25 * l)]]

    right = [ranges[int(0.75 * l)], ranges[-1]]

    #print(left, middle, right) # print if needed. 
    if middle < 1: # if middle < 1, turn left. 
        t.angular.z = 0.6
        t.linear.x = 0.2
    
    elif (right[0] < 1 or right[1] < 1) and middle >= 1: # if right is less than 1m but middle is >1, still go left
        t.angular.z = -0.6
        t.linear.x = 0.2
    
    elif (left[0] < 1 or left[1] < 1) and middle >=1:  # if left is less than 1m but middle is >1, still go right
        t.angular.z = 0.6
        t.linear.x = 0.2

    else: # if no obstacle anywhere, keep moving forward by default. 
        t.linear.x = 0.2
        t.angular.z = 0.0


while not rospy.is_shutdown():
    pub.publish(t) # send velocity commands to robot
    sub = rospy.Subscriber("kobuki/laser/scan", LaserScan, callback) # read velocity commands. 
    rate.sleep()
