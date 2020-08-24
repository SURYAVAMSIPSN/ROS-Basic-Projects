This assignment uses the concept of ROSTOPICS and ROSMSGS to give velocity commands to a Kobuki Robot. 

Instructions: 
1. Download the my_turtlebot package into your catkin_ws/src folder to get the python scripts in the src folder of the package.
2. The .py file is "simple_topic_publisher.py" inside the src folder of the my_turtlebot package.
3. Launch file is in the launch folder of the same package. 
4. run the command: roslaunch my_turtlebot my_turtlebot_launch_file.launch
5. Make sure to.. have fun. :)

ROSTOPIC used here is /cmd_vel

The robot gets commands through the message type called Twist. 

Twist has Linear (x, y and z) and Angular (x, y and z) Velocities. 

For this example, since it's a simulation in Gazebo, the linear x and angular z alone are assigned values for moving the robot. (Change values as per your wish)

NOTE: This has been done on the simulator provided by The Construct (Robot Ignite Academy). So, everything done here doesn't work exactly so if you implement it on your PC. 

You need to make some changes accordingly. The launch file and .py files need not be changed. 
