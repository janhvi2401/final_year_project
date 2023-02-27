import rospy 
from cv_bridge import CvBridge
import cv2 
from sensor_msgs.msg import Image 

rospy.init_node("webcam_node",anonymous = True)

pub = rospy.Publisher("/webcam_data",Image)
video = cv2.VideoCapture(0) 

success = True

bridge = CvBridge()
while success:
    success,image= video.read()
    ros_image = bridge.cv2_to_imgmsg(image,"bgr8")
    pub.publish(ros_image)
    cv2.imshow("webcam",image)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

