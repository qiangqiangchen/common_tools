# -*- coding: utf-8 -*-
"""计算并绘制直方图"""
"""
直方图
目标：
1.%s
2.OpenCV函数：cv2.calcHist(), cv2.equalizeHist()

"""
import cv2
import matplotlib.pyplot as plt

import numpy as np
from functools import reduce
import random


# 模板匹配
def f1():
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\bage.jpeg', 0)
    template = cv2.imread(r'E:\pycharmproject\pythonlearn\image\head.jpg', 0)
    h, w = template.shape[:2]

    # 相关系数匹配方法：
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    left_top = max_loc  # 左上角
    right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
    cv2.rectangle(img, left_top, right_bottom, 255, 2)

    cv2.imshow("temp", img)
    cv2.waitKey(0)


# 匹配多个物体
def f2():
    img = cv2.imread(r'F:\dd\20191225191407.jpg')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(r'F:\dd\0.jpg', 0)
    h, w = template.shape[:2]

    # 标准相关模块匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8

    #
    loc = np.where(res >= threshold)  # 匹配程度大于80%的坐标y,x
    for pt in zip(*loc[::-1]):  # *表示可选参数
        right_bottom = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img, pt, right_bottom, (0, 0, 255), 2)

    cv2.imshow("temp", img)
    cv2.waitKey(0)


def f3():
    img = cv2.imread(r'F:\dd\20191225191407.jpg')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


if __name__ == "__main__":
    f2()
