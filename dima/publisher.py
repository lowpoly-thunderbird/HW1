#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def publish():
    pub = rospy.Publisher('joint_states',JointState, queue_size=10)
    rospy.init_node('publish', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.header.frame_id = 'pub'   
    hello_str.name = ['base_to_first_link', 'first_link_to_second_link', 'second_link_to_third_link']
#    hello_str.velocity = []
#    hello_str.effort = []
    a = 0.0
    b = 0.0
    c = 0.0
    flag_1 = True
    flag_2 = True
    flag_3 = True
    while not rospy.is_shutdown():
	    
	    hello_str.header.stamp = rospy.Time.now()
	    hello_str.position = [a, b, c]
	    if flag_2:
	        c = c + 0.1
	        if c > 2.39:
	            flag_2 = False   
	    else:
	        c = c - 0.1
	        if c < -2.30:
	            flag_2 = True
	    
	    if flag_1:
	        a = a + 0.1
	        if a > 1.1:
	            flag_1 = False   
	    else:
	        a = a - 0.1
	        if a < -1.1:
	            flag_1 = True
	        
	    if flag_3:
	        b = b + 0.1
	        if b > 1.90:
	            flag_3 = False   
	    else:
	        b = b - 0.1
	        if b < -1.90:
	            flag_3 = True
	            
	    pub.publish(hello_str)
	    rate.sleep()

if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass
