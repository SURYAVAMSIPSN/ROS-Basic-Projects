#! /usr/bin/env python

# This is the Client. 
import rospy
import rospkg
# Import the service message used by the service /execute_trajectory
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest 
import sys

# Initialise a ROS node with the name McNugget_Client
rospy.init_node('McNugget_Client')
rospack = rospkg.RosPack()
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')
# Create the connection to the service
exec_traj_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
# Create an object of type ExecTrajRequest
exec_traj_object = ExecTrajRequest()
# Fill the variable "file" of this object with the desired value
exec_traj_object.file = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
# Send through the connection the name of the trajectory to be executed by the robot
result = exec_traj_service(exec_traj_object)
# Print the result given by the service called
print(result)