#! /usr/bin/env python 

import rospy
from bb8_class.srv import ClassServiceMessage, ClassServiceMessageRequest


rospy.init_node('move_in_circle_client')

rospy.loginfo("waiting for service ...")
rospy.wait_for_service('/move_in_circle')

my_service = rospy.ServiceProxy('/move_in_circle', ClassServiceMessage)

service_object = ClassServiceMessageRequest()

service_object.time = 20
result = my_service(service_object) 
print(result)

rospy.loginfo("done")