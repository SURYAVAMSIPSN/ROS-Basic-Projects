#! /usr/bin/env python

# This is the Client. 
import rospy
import sys
from std_srvs.srv import Empty, EmptyRequest

# Initialise a ROS node with the name bb8_Client
rospy.init_node('bb8_client')
# Wait for the service client to be running
rospy.wait_for_service('/move_bb8_in_circle')
# Create the connection to the service
move_circle_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
move_object = EmptyRequest()
result = move_circle_service(move_object)
# Print the result given by the service called
print(result)