This assignment uses the concept of ROSTOPICS and ROSMSGS to give velocity commands to a Kobuki Robot. 

Download the my_turtlebot package into your catkin_ws/src folder to get the python scripts in the src folder of the package.

ROSTOPIC used here is /cmd_vel

The robot gets commands through the message type called Twist. 

Twist has Linear (x, y and z) and Angular (x, y and z) Velocities. 

For this example, since it's a simulation in Gazebo, the linear x and angular z alone are assigned values for moving the robot. (Change values as per your wish)

NOTE: This has been done on the simulator provided by The Construct (Robot Ignite Academy). So, everything done here doesn't work exactly so if you implement it on your PC. 

You need to make some changes accordingly. The launch file and .py files need not be changed. 
