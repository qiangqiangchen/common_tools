# -*- coding: utf-8 -*-
"""
阈值分割
目标：
1.使用固定阈值、自适应阈值和Otsu阈值法”二值化”图像
2.OpenCV函数：cv2.threshold(), cv2.adaptiveThreshold()

"""
import numpy as np
import matplotlib.pyplot as plt

import cv2


def getshape():
    img = cv2.imread(r'F:\dd\20191225191407.jpg', 0)
    # 阈值分割
    # cv2.threshold()需要传入4个参数
    # 1. 原图，一般是灰度图
    # 2. 设定的阈值
    # 3. 最大阈值，一般为255
    # 4. 阈值的方式，主要有5种
    ret, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    # cv2.namedWindow("thresh", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("thresh", 600, 450)
    cv2.imshow("img", img)
    cv2.imshow("thresh", th)
    cv2.waitKey(0)


# 固定阈值分割
def threshold():
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\002.jpg', 0)

    # 应用5中不同的阈值方法
    ret, th1 = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
    ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, th3 = cv2.threshold(img, 210, 255, cv2.THRESH_TRUNC)
    ret, th4 = cv2.threshold(img, 210, 255, cv2.THRESH_TOZERO)
    ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    title = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, th1, th2, th3, th4, th5]

    # 使用matplotlib显示

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(title[i], fontsize=8)
        plt.xticks([]), plt.yticks([])
    plt.show()


# 自适应阈值
def adaptiveThreshold():
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\002.jpg', 0)
    # 固定阈值
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # 自适应阈值
    # 参数1：原图
    # 参数2：最大阈值，一般为255
    # 参数3：小区域的计算方法
    #       ADAPTIVE_THRESH_MEAN_C：小区域内取均值
    #       ADAPTIVE_THRESH_GAUSSIAN_C：小区域内加权求和，权重是个高斯核
    # 参数4：阈值方式（前面说的5种）
    # 参数5：小区域的面积，如11就是11*11
    # 参数6：最终阈值等于小区域计算出的阈值再减去此值
    #
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 4)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)

    title = ['Original', 'Global(v = 127)', 'Adaptive Mean', 'Adaptive Gaussian']
    images = [img, th1, th2, th3]

    # 使用matplotlib显示

    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i], 'gray')
        plt.title(title[i], fontsize=8)
        plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    getshape()
