# -*- coding: utf-8 -*-
"""
边缘检测
目标：
1.Canny边缘检测的简单概念
2.OpenCV函数：cv2.Canny()

"""
import cv2
import matplotlib.pyplot as plt

import numpy as np


def f1():
    """
    Canny边缘检测
    :return:
    """
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\sudoku.jpg', 0)
    # 参数2,3分别表示最低、最高阈值
    edges = cv2.Canny(img, 50, 120)
    cv2.imshow("img", edges)
    cv2.waitKey(0)


"""
图像梯度
"""


def f2():
    """
    垂直边缘提取
    :return:
    """
    img2 = cv2.imread(r'E:\pycharmproject\pythonlearn\image\sudoku.jpg', 0)

    # 自己进行垂直边缘提取
    kernel = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]], dtype=np.float32
    )
    dst_v = cv2.filter2D(img2, -1, kernel)
    # 水平边缘提取
    dst_h = cv2.filter2D(img2, -1, kernel.T)

    # 横向并列对比显示
    cv2.imshow('edge', np.hstack((img2, dst_v, dst_h)))


    #直接使用cv2.Laplacian()函数
    laplacian=cv2.Laplacian(img2,-1)
    cv2.imshow('laplacian', np.hstack((img2, laplacian)))

    cv2.waitKey(0)


"""
Sobel算子
"""

def f3():
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\sudoku.jpg', 0)
    def nothing(x):
        pass
    cv2.namedWindow('image')

    cv2.createTrackbar('min', 'image', 0, 255, nothing)
    cv2.createTrackbar('max', 'image', 0, 255, nothing)

    while(1):
        min=cv2.getTrackbarPos('min', 'image')
        max=cv2.getTrackbarPos('max', 'image')
        edges=cv2.Canny(img,min,max)
        cv2.imshow('image', edges)
        if cv2.waitKey(30) == 27:
            break

if __name__ == "__main__":
    f3()
