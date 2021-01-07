# -*- coding: utf-8 -*-
"""
图像混合
目标：
1.图片间的数学运算，如相加、按位运算等
2.OpenCV函数：cv2.add(), cv2.addWeighted(), cv2.bitwise_and()

"""
import time

import cv2

import numpy as np


def add():
    """
        图片相加
        :return:
        """
    x = np.uint8([250])
    y = np.uint8([10])
    print(cv2.add(x, y))
    print(x + y)


def f2():
    """
    图片混合
    :return:
    """
    img1 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\001.jpg')
    img2 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\002.jpg')
    res = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)
    # res2 = cv2.add(img1, img2)
    cv2.imshow("test", res)
    # cv2.imshow("test2", res2)
    cv2.waitKey(0)

def f2_1():
    img1 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\001.jpg')
    img2 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\002.jpg')
    index=1
    while(1):
        index-=0.01
        res = cv2.addWeighted(img1, index, img2, 1-index, 0)
        cv2.imshow("test", res)

        if cv2.waitKey(80) == 27:
            break


def f3():
    """
    按位操作
    如果将两幅图片直接相加会改变图片的颜色，如果用图像混合，则会改变图片的透明度，所以需要按位操作
    :return:
    """
    img1 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\bage.jpeg')
    # img2 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\opencv-logo-white.png')
    img2 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\logo.jpg')
    rows, cols = img2.shape[:2]
    roi = img1[:rows, :cols]

    # 创建掩膜
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 使用阈值切割logo图片，分别得到背景和logo的掩膜
    ret, mask = cv2.threshold(img2gray, 160, 255, cv2.THRESH_BINARY)
    cv2.imshow("mask", mask)

    mask_inv = cv2.bitwise_not(mask)
    cv2.imshow("mask_inv", mask_inv)

    # 原图和logo的掩膜位相加，得到背景为原图，logo位置为黑色的图片
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
    cv2.imshow("img1_bg", img1_bg)
    # logo图片和logo背景位相加，得到背景为黑色，保留logo颜色的图片
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
    cv2.imshow("img2_fg", img2_fg)
    # 进行融合
    dst = cv2.add(img1_bg, img2_fg)
    cv2.imshow("dst", dst)
    # 将融合后的图片放入原图中
    img1[:rows, :cols] = dst
    cv2.imshow("test2", img1)
    cv2.waitKey(0)


def f4():
    img1 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\001.jpg')
    img2 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\002.jpg')

    # 创建掩膜
    img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    ret, mask = cv2.threshold(img2Gray, 200, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    cv2.imshow("test1", mask)

    blur=cv2.blur(mask,(5,5))
    median=cv2.medianBlur(mask,5)
    cv2.imshow("blur", blur)
    cv2.imshow("median", median)
    cv2.imshow("test2", mask_inv)
    img1bg = cv2.bitwise_and(img1, img1, mask=mask_inv)
    img2bg = cv2.bitwise_and(img2, img2, mask=mask)
    temp = cv2.add(img1bg, img2bg)

    # cv2.imshow("test3", img1bg)
    cv2.imshow("test4", temp)
    cv2.waitKey(0)


if __name__ == "__main__":
    f4()
