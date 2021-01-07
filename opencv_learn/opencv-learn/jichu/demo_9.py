# -*- coding: utf-8 -*-
"""
直方图
目标：
1.计算并绘制直方图
2.OpenCV函数：cv2.calcHist(), cv2.equalizeHist()

"""
import cv2
import matplotlib.pyplot as plt

import numpy as np
from functools import reduce
import random
def f1():
    """
    使用cv2.calcHist(images, channels, mask, histSize, ranges)计算，其中：

    参数1：要计算的原图，以方括号的传入，如：[img]
    参数2：类似前面提到的dims(要计算的通道数，对于灰度图dims=1，普通彩色图dims=3)，灰度图写[0]就行，彩色图B/G/R分别传入[0]/[1]/[2]
    参数3：要计算的区域，计算整幅图的话，写None
    参数4：前面提到的bins（子区段数目，如果我们统计0~255每个像素值，bins=256；如果划分区间，比如0~15, 16~31…240~255这样16个区间，bins=16）
    参数5：前面提到的range（要计算的通道数，对于灰度图dims=1，普通彩色图dims=3）
    :return:
    """

    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\bage.jpeg')

    b_hist=cv2.calcHist([img],[0],None,[256],[0,256])
    g_hist=cv2.calcHist([img],[1],None,[256],[0,256])
    r_hist=cv2.calcHist([img],[2],None,[256],[0,256])

    # cv2.imshow("temp", img)
    # cv2.waitKey(0)
    plt.plot(b_hist,color='b')
    plt.plot(g_hist,color='g')
    plt.plot(r_hist,color='r')
    plt.show()

def f2():
    """
    直方图均衡化:直方图均衡化就是用来改善图像的全局亮度和对比度
    :return:
    """
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\small.jpg',0)
    #直方图均衡化
    equ=cv2.equalizeHist(img)
    #自适应均衡化，参数可选
    clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    cl1=clahe.apply(img)
    cv2.imshow("temp", np.hstack((img,equ,cl1)))
    cv2.waitKey(0)


if __name__ == "__main__":
    f2()
