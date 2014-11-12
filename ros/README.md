### ROS (Robot Operating System) Python (rospy) pub/sub example.

#### Create catkin workspace

Done once.

```
source /opt/ros/indigo/setup.bash  # should go in .bashrc
mkdir ros  # this directory is considered 'catkin workspace'
cd ros  
mkdir -p src
cd src
catkin_init_workspace
cd ..
catkin_make
```

#### Create ROS package

Creates `CMakeLists.txt` and `src/ros_pub_sub/` stuff, mainly `package.xml`
package definition. ROS package name is `ros_pub_sub`. Specify dependencies.

```
cd src 
catkin_create_pkg ros_pub_sub std_msgs rospy
```

#### Development

from the main `ros` directory:

```
cd src/ros_pub_sub/src
```

Put codes in this directory. Tutorials tend put Python codes into
`scripts` directory, doesn't seem to matter. 


#### Build ROS package

```
cd ros  # the main project root directory
catkin_make
```


#### Running

`roscore`

starts `roslaunch`, `rosmaster` servers:
```
started roslaunch server http://localhost:44424/
ROS_MASTER_URI=http://localhost:11311/
rosout:38198 (std[out,err])
rosout::45277
```

##### Publisher

```
cd ros
source devel/setup.bash
rosrun ros_pub_sub publisher.py
```

##### Subscriber

```
cd ros
source devel/setup.bash
rosrun ros_pub_sub subscriber.py
```


Without creating the package, `rosrun` would complain it can't find
the package. Then the Python codes has to be in the package tree, otherwise
`rosrun` complains it can't find these executables. They have to have `+x`
flag set.


##### Check

Run `rostopic list` while the publisher is run.