# -*- coding: utf-8 -*-
"""
轮廓特征
目标：
1.计算物体的周长、面积、质心、最小外接矩形
2.OpenCV函数：cv2.contourArea(), cv2.arcLength(), cv2.approxPolyDP() 等

"""
import cv2
import matplotlib.pyplot as plt

import numpy as np
from functools import reduce
import random
def f1():
    """
    寻找轮廓
    :return:
    """

    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\handwriting.jpg')

    # #阈值分割
    ret, mask = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 50, 250, cv2.THRESH_BINARY_INV)
    # #平滑图像
    median = cv2.medianBlur(mask, 5)
    image, contours, hierarchy = cv2.findContours(median, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[1]

    cv2.drawContours(img, [cnt], 0, (0, 0, 255), 3)
    # 轮廓面积
    area = cv2.contourArea(cnt)
    print(area)
    # 轮廓周长
    perimeter = cv2.arcLength(cnt, True)
    print(perimeter)
    # 图像矩,炬可以理解为图形的各类几何特征
    M = cv2.moments(cnt)
    print(M)

    # 外接矩形
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 最小外接矩形
    rect = cv2.minAreaRect(cnt)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(img, [box], 0, (255, 0, 0), 2)

    # 最小外接圆
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    (x, y, radius) = np.int0((x, y, radius))
    cv2.circle(img, (x, y), radius, (0, 0, 255), 2)

    # 拟合椭圆
    ellipsis = cv2.fitEllipse(cnt)
    cv2.ellipse(img, ellipsis, (255, 255, 0), 2)

    cv2.imshow("temp", img)
    cv2.waitKey(0)


def f2():
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\shapes.jpg', 0)
    # 阈值切割
    _, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    # 寻找轮廓
    image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
    image_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # 比较形状
    cnt_a, cnt_b, cnt_c = contours[0], contours[1], contours[2]
    cv2.drawContours(image_color, [cnt_c], 0, (0, 255, 0), 2)
    cv2.drawContours(image_color, [cnt_b], 0, (0, 255, 0), 2)
    print(cv2.matchShapes(cnt_b, cnt_b, 1, 0.0))
    print(cv2.matchShapes(cnt_b, cnt_a, 1, 0.0))
    print(cv2.matchShapes(cnt_b, cnt_c, 1, 0.0))

    cv2.imshow("temp", image_color)
    cv2.waitKey(0)



#自动找出相似度高的轮廓
def f3():
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\t5.png', 0)
    # 阈值切割
    _, thresh = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
    temp = cv2.medianBlur(thresh, 5)

    # 寻找轮廓
    image, contours, hierarchy = cv2.findContours(thresh, 3, 2)
    image_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    result=[]
    for i in range(len(contours)):
        sim=100
        index=0
        for j in range(len(contours)):
            if i==j:
                pass
            else:
                arg = cv2.matchShapes(contours[i], contours[j], 1, 0.0)
                if arg<sim:
                    sim=arg
                    index=j
        if result.count((i,index))>0:
            pass
        elif result.count((i,index)[::-1])>0:
            pass
        else:
            result.append((i, index))

    print(result)
    for i in result:
        color=random.randint(0,255)
        color2=random.randint(0,100)
        color3=random.randint(80,170)
        cv2.drawContours(image_color, [contours[i[0]]], 0, (color3, 0, color2), 2)
        cv2.drawContours(image_color, [contours[i[1]]], 0, (color3, 0, color2), 2)

    cv2.imshow("temp", image_color)
    cv2.waitKey(0)


if __name__ == "__main__":
    f3()
    # l=[(1, 6.730473938451603), (2, 0.3114657167712158), (3, 6.54371844636109)]
    # print(sorted(l,key=lambda x:x[1]))

