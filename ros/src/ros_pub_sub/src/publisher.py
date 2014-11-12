#!/usr/bin/env python

# rosrun requires executable flag and the first line


import rospy
from std_msgs.msg import String  # also rospy thing


def publisher():
    pub = rospy.Publisher("publisher", String, queue_size=10)
    rospy.init_node("publisher""", anonymous=True)
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = "hello world %s" % rospy.get_time()
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()


if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass