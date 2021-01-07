# -*- coding: utf-8 -*-
"""
轮廓
目标：
1.寻找并绘制轮廓
2.OpenCV函数：cv2.findContours(), cv2.drawContours()

"""
import cv2
import matplotlib.pyplot as plt

import numpy as np




def f1():
    """
    寻找轮廓
    :return:
    """

    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\handwriting.jpg' )

    # #阈值分割
    ret, mask = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY), 50, 250, cv2.THRESH_BINARY_INV)
    # #平滑图像
    median = cv2.medianBlur(mask, 5)
    cv2.imshow("temp", img)
    # 使用cv2.findContours()寻找轮廓
    # 参数2：轮廓的查找方式，一般使用cv2.RETR_TREE，表示提取所有的轮廓并建立轮廓间的层级, RETR_LIST: 它不建立轮廓间的子属关系，也就是所有轮廓都属于同一层级
    #  RETR_EXTERNAL:这种方式只寻找最高层级的轮廓;它把所有的轮廓只分为2个层级，不是外层的就是里层的它把所有的轮廓只分为2个层级，不是外层的就是里层的
    # 参数3：轮廓的近似方法。比如对于一条直线，我们可以存储该直线的所有像素点，也可以只存储起点和终点。使用cv2.CHAIN_APPROX_SIMPLE就表示用尽可能少的像素点表示轮廓
    # 函数有3个返回值，image还是原来的二值化图片，hierarchy是轮廓间的层级关系,我们主要看contours，它就是找到的轮廓了，以数组形式存储，记录了每条轮廓的所有像素点的坐标(x,y)
    image, contours, hierarchy = cv2.findContours(median, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    #绘制轮廓
    #其中参数2就是得到的contours，参数3表示要绘制哪一条轮廓，-1表示绘制所有轮廓，参数4是颜色（B/G/R通道，所以(0,0,255)表示红色），参数5是线宽
    cv2.drawContours(img,contours,-1,(0,0,255),5)
    cv2.imshow("temp", img)
    cv2.waitKey(0)


def f2():

    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\yuan.png')
    temp=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,mask=cv2.threshold(temp,50,256,cv2.THRESH_BINARY)
    median=cv2.medianBlur(mask,5)

    image,contours,hierarchy=cv2.findContours(median,cv2.RETR_CCOMP,2)
    print(len(contours))
    # print(hierarchy)
    for i in range(len(contours)):
        if (hierarchy[0][i][2]<0):
            cnt = contours[i]
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)


    # cv2.imshow("temp", median)
    cv2.imshow("image", img)
    cv2.waitKey(0)

if __name__ == "__main__":
    f2()
