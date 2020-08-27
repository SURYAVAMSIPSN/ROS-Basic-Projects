#! /usr/bin/env python

from move_in_circle import BB8
import rospy
from bb8_class.srv import ClassServiceMessage, ClassServiceMessageResponse

def callback(request):
    response = ClassServiceMessageResponse()
    time = request.time  # integer value.
    movebb8_object = BB8()
    movebb8_object.move_with_time(0.5, 0.5, time)
    response.success = True
    return response

rospy.init_node('move_in_circle_server')
rospy.loginfo("started service.BB8")
service = rospy.Service('/move_in_circle', ClassServiceMessage, callback)
rospy.spin()
    
