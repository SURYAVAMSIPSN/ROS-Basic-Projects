#! /usr/bin/env python 

import rospy
from bb8_2.srv import CustomServiceMessage, CustomServiceMessageRequest

rospy.init_node('bb8_2_client')

rospy.wait_for_service('/move_bb8_in_circle_custom')

service = rospy.ServiceProxy('/move_bb8_in_circle_custom', CustomServiceMessage)

move_object = CustomServiceMessageRequest()
move_object.duration = 40 # Duration of movement
result = service(move_object)
print(result)