# -*- coding: utf-8 -*-
"""
颜色空间转换
目标：
1.颜色空间转换，如BGR<->Gray,BGR<->HSV等
2.追踪视频中特定颜色的物体

"""
import numpy as np

import cv2


def getshape():
    capture = cv2.VideoCapture(r"..\image\demo.mp4")
    # 黄色的范围，不同光照条件下不一样
    low_yello = np.array([0,1,2])
    upper_yello = np.array([0,255,255])

    while (capture.isOpened()):
        # 1.逐帧获取
        ref, frame = capture.read()
        if not ref:
            break

        # 2.从BGR转换为HVS
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 3.inrange():介于lower/upper之间的为白色，其他为黑色
        mask = cv2.inRange(hsv, low_yello, upper_yello)

        # 只保留原图中的黄色部分
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        if cv2.waitKey(30) == ord('q'):
            break

if __name__ == "__main__":
    getshape()
    # yello=np.uint8([[[0,0,255]]])
    # hsv_yello=cv2.cvtColor(yello,cv2.COLOR_BGR2HSV)
    # print(hsv_yello)