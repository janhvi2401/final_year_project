import rospy 
from sensor_msgs.msg import Image 

rospy.init_node("node_webcam", anonymous = True)


def cb(data):
    Height = data.height
    Width = data.width
    print("Height = ", Height,"Width = ", Width)

sub = rospy.Subscriber("/webcam_data", Image, cb)
 
rospy.spin()


 