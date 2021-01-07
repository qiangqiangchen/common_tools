# -*- coding: utf-8 -*-
"""
边缘检测
目标：
1.图片融合
2.OpenCV函数：cv2.cvtColor(),cv2.threshold(),cv2.medianBlur(),cv2.morphologyEx(),cv2.bitwise_not(),cv2.bitwise_and(),cv2.add()
思路：
1.
"""

import cv2

import numpy as np


def f4():
    img1 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\001.jpg')
    img2 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\002.jpg')

    # 创建掩膜
    img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    ret, mask = cv2.threshold(img2Gray, 200, 255, cv2.THRESH_BINARY)
    median = cv2.medianBlur(mask, 5)




    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    closing = cv2.morphologyEx(median, cv2.MORPH_OPEN, kernel1)
    mask_inv = cv2.bitwise_not(closing)
    cv2.imshow("closing", closing)
    cv2.imshow("mask_inv", mask_inv)
    img1bg = cv2.bitwise_and(img1, img1, mask=mask_inv)
    img2bg = cv2.bitwise_and(img2, img2, mask=closing)
    temp = cv2.add(img1bg, img2bg)

    cv2.imshow("img1bg", img1bg)
    cv2.imshow("img2bg", img2bg)
    cv2.imshow("test4", temp)
    cv2.waitKey(0)



def f5():
    img=cv2.imread(r"E:\test.png")
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret,thresh=cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
    median = cv2.medianBlur(thresh, 5)
    cv2.imshow("img1bg", median)
    cv2.waitKey(0)


if __name__=="__main__":
    f5()