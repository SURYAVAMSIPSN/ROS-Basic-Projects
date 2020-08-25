This is a short quiz in which a robot is required to avoid a wall (Obstacle Avoidance) using topics, publishers and subscriber
Run the launch file in the launch folder to watch the robot move towards a stationary wall and avoid it by turning left. 

The python script is based on pubs, subs, topics and messages. The goal for the robot is to detect the range of the wall using the LaserScan message as a subscriber, and 
give velocity commands to the robot using the Twist message as a publisher over the topic /cmd_vel. The ranges array of Laser scanner contains obstacle range in front (middle
elements), left side (initial elements) and right side (last elements of array) of robot. If any of it is < 1m, the robot needs to avoid it. 

Again, this was run on the simulator given by Robot Ignite Academy. Kindly make changes if you want to run it on your local PC. 



