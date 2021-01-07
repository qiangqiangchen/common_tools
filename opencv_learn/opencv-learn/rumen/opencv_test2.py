# -*- coding: utf-8 -*-
"""
绘制
目标：
1.使用鼠标绘图
"""
import datetime
import math

import numpy as np
import matplotlib.pyplot as plt
import cv2

# 获取鼠标的事件
img = np.zeros((512, 512, 3), np.uint8)
drawing = False
start = (-1, -1)

def mouse_ecent(event, x, y, flags, param):
    global start, drawing,img
    if event == cv2.EVENT_LBUTTONDOWN:
        print("mouse left button down:({},{}".format(x, y))
        drawing = True
        start = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        print("mouse left button up:({},{})".format(x, y))
        drawing = False
        img = np.zeros((512, 512, 3), np.uint8)
        cv2.rectangle(img, start, (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_MOUSEMOVE:

        if drawing:
            img = np.zeros((512, 512, 3), np.uint8)
            cv2.rectangle(img, start, (x, y), (0, 255, 0), 2)
            print("mouse left button move:({},{})".format(x, y))
        else:
            print("stop move")


cv2.namedWindow("image")
cv2.setMouseCallback('image', mouse_ecent)
while (True):
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 27:
        break
