#! /env/bin/env python

import rospy

rospy.init_node("McFries_Publisher")
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) # name of topic
rate = rospy.rate(2)


var = Twist() # Twist has linear x, y, z and angular x, y and z. 
# All are float64. 

# For this example, x is linear, z is angular. 

while not rospy.is_shutdown():
    var.linear.x = 0.5
    var.angular.z = 0.5 # assign linear and angular velocities to the x and z values. 
    pub.publish(var)
    rate.sleep()
