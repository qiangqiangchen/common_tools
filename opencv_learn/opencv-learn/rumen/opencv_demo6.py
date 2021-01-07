# -*- coding: utf-8 -*-
"""
图像几何变化
目标：
1.实现旋转、平移和缩放
2.OpenCV函数：cv2.resize(), cv2.flip(), cv2.warpAffine()

"""
import numpy as np
import matplotlib.pyplot as plt

import cv2


# 缩放图片
def resize():
    img = cv2.imread(r"..\image\bage.jpeg", 0)

    # 按照指定的宽度、高度缩放图片
    res = cv2.resize(img, (640, 480))
    # 按照比例缩放，x,y轴均放大一倍
    res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("test", img)
    cv2.imshow("resize", res2)
    cv2.waitKey(0)


# 翻转图片
def flip():
    img = cv2.imread(r"..\image\bage.jpeg", 0)

    # 按照指定的宽度、高度缩放图片
    # 参数2 = 0：垂直翻转(沿x轴)，参数2 > 0: 水平翻转(沿y轴)，参数2 < 0: 水平垂直翻转。
    res = cv2.flip(img, 2)

    cv2.imshow("test", img)
    cv2.imshow("resize", res)
    cv2.waitKey(0)


# 平移图片
def warpAffine():
    import numpy as np

    img = cv2.imread(r"..\image\bage.jpeg", 0)
    rows, cols = img.shape[:2]

    # 定义平移矩阵，需要是numpy的float32类型
    # x轴平移100，y轴平移50
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    # 用仿射变换实现平移
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow("old", img)
    cv2.imshow("demo", dst)
    cv2.waitKey(0)


# 旋转图片

def Rotation():
    img = cv2.imread(r"..\image\bage.jpeg", 0)
    rows, cols = img.shape[:2]
    # 45度旋转图片并缩小一半
    # getRotationMatrix2D()函数生成变化矩阵，需要传入3个参数
    # 参数1：图片的旋转中心
    # 参数2：旋转角度，正：逆时针，负：顺时针
    # 参数3：缩放比例，0.5表示缩小一半
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.5)
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow("demo", dst)
    cv2.waitKey(0)


if __name__ == "__main__":
    Rotation()
