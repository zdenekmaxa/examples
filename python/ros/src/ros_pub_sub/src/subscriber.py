#!/usr/bin/env python

# rosrun requires executable flag and the first line


import rospy
from std_msgs.msg import String  # also rospy thing


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " received msg: '%s'" % data.data)


def subscriber():
    # in ROS, nodes are unique named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'publisher' node so that multiple talkers can
    # run simultaneously.
    rospy.init_node("subscriber", anonymous=True)
    rospy.Subscriber("publisher", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == "__main__":
    subscriber()