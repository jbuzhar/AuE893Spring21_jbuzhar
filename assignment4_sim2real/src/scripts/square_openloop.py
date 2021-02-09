#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi

def square_openloop():
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Define the linear and angular velocities
    linvel = 0.2	# Units / second
    angvel = 0.2	# Rad / s

    # Drive straight for 2 units
    vel_msg.linear.x = linvel
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    relative_distance = 2
    
    while(current_distance < relative_distance):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = linvel*(t1-t0)
        
    # Rotate 90 degrees
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angvel
    
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    relative_angle = pi/2
    
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angvel*(t1-t0)
        
    # Drive straight for 2 units
    vel_msg.linear.x = linvel
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    relative_distance = 2
    
    while(current_distance < relative_distance):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = linvel*(t1-t0)
        
    # Rotate 90 degrees
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angvel
    
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    relative_angle = pi/2
    
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angvel*(t1-t0)
        
    # Drive straight for 2 units
    vel_msg.linear.x = linvel
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    relative_distance = 2
    
    while(current_distance < relative_distance):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = linvel*(t1-t0)
        
    # Rotate 90 degrees
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angvel
    
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    relative_angle = pi/2
    
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angvel*(t1-t0)
    
    # Drive straight for 2 units
    vel_msg.linear.x = linvel
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    relative_distance = 2
    
    while(current_distance < relative_distance):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = linvel*(t1-t0)
        
    # Rotate 90 degrees
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angvel
    
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    relative_angle = pi/2
    
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angvel*(t1-t0)

    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()

if __name__ == '__main__':
    try:
        # Testing our function
        square_openloop()
    except rospy.ROSInterruptException:
        pass

