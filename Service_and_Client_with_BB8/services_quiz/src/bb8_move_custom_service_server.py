#! /usr/bin/env python 

import rospy 
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
import time

rospy.init_node('bb8_server')
move = Twist()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(1)
count = 0

def linear_movement(move):
    move.linear.x = 0.5
    move.angular.z = 0.0
    return move

def angular_movement(move):
    move.linear.x = 0.0
    move.angular.z = 0.923
    return move

def halt(move):
    move.linear.x = 0.0
    move.angular.z = 0.0
    return move


def callback(request):
    response = BB8CustomServiceMessageResponse()
    global count
    
    linear_time = request.side / 0.5
    
    n = request.repetitions * 4

    while count < n: # repeat this many times
        # move in square here. 
        pub.publish(halt(move))
        time.sleep(0.1)
        
        pub.publish(linear_movement(move))
        time.sleep(linear_time)
        pub.publish(halt(move))
        time.sleep(0.1)
        pub.publish(angular_movement(move))
        time.sleep(1.7)
        pub.publish(halt(move))
        time.sleep(0.1)
        
        count += 1

    pub.publish(halt(move))
    response.success = True
    return response

service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, callback)
rospy.spin()