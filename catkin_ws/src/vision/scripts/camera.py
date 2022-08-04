#!/usr/bin/env python3

import os
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


IMAGE_STORAGE = "/home/mikhail/image_storage"
STORING = False

cap = cv2.VideoCapture(0)
bridge = CvBridge()
print(f"Camera is ready: {cap.isOpened()}")

def talker() -> None:
    global cap, bridge, STORING, IMAGE_STORAGE
    if STORING:
        img_counter = 0
        if not os.path.exists(IMAGE_STORAGE):
            raise RuntimeError(f"Please create the storage folder, ROS can't do it - {IMAGE_STORAGE}")

    pub = rospy.Publisher('/usbcam', Image, queue_size=1)
    rospy.init_node('image', anonymous=False)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            break

        msg = bridge.cv2_to_imgmsg(frame, 'bgr8')
        pub.publish(msg)

        if STORING:
            cv2.imwrite(f"{IMAGE_STORAGE}/{img_counter}.jpg", frame)
            img_counter += 1

        if rospy.is_shutdown():
            cap.release()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
