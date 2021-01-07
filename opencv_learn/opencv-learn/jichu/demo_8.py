# -*- coding: utf-8 -*-
"""
轮廓特征
目标：
1.凸包及更多轮廓特征
2.OpenCV函数：cv2.contourArea(), cv2.arcLength(), cv2.approxPolyDP() 等

"""
import cv2
import matplotlib.pyplot as plt

import numpy as np
from functools import reduce
import random
def f1():
    """
    多边形逼近
    :return:
    """

    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\heand.jpg')

    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # #阈值分割

    ret, mask = cv2.threshold(img, 150, 250, cv2.THRESH_BINARY_INV)
    # cv2.imshow("img", mask)
    # # #平滑图像

    median = cv2.medianBlur(mask, 5)
    image, contours, hierarchy = cv2.findContours(median, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_color=cv2.cvtColor(median,cv2.COLOR_GRAY2BGR)
    print(len(contours))
    cv2.drawContours(img_color,contours,-1,(0,0,255),2)

    #多边形逼近，得到多边形的角点
    #参数2(epsilon)是一个距离值，表示多边形的轮廓接近实际轮廓的程度，值越小，越精确；参数3表示是否闭合
    approx=cv2.approxPolyDP(contours[0],8,True)
    cv2.polylines(img_color,[approx],True,(0,255,0),2)


    #凸包
    #凸包跟多边形逼近很像，只不过它是物体最外层的”凸”多边形
    #寻找凸包，得到凸包的角点


    #其中函数cv2.convexHull()有个可选参数returnPoints，默认是True，代表返回角点的x/y坐标；如果为False的话，表示返回轮廓中是凸包角点的索引
    hull=cv2.convexHull(contours[0])
    cv2.polylines(img_color,[hull],True,(0,255,255),2)

    cv2.imshow("temp", img_color)
    cv2.waitKey(0)




if __name__ == "__main__":
    f1()
