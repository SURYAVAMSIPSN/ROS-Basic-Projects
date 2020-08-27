#! /usr/bin/env python 
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('bb8_client')

rospy.wait_for_service('/move_bb8_in_square_custom')

service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)

service_object = BB8CustomServiceMessageRequest()
service_object.side = 2
service_object.repetitions = 1

result = service(service_object)
print(result)