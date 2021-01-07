# -*- coding: utf-8 -*-
"""霍夫变换"""
"""
目标：
1.理解霍夫变换的实现
2.分别使用霍夫线变换和圆变换检测图像中的直线和圆
3.OpenCV函数：cv2.HoughLines(), cv2.HoughLinesP(), cv2.HoughCircles()

"""
import cv2
import matplotlib.pyplot as plt

import numpy as np
from functools import reduce
import random


# 霍夫直线变换
def f1():
    #1.加载图片，转为二值化
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\shape.jpg')
    drawing = np.zeros(img.shape[:], dtype=np.uint8)
    drawing2 = np.zeros(img.shape[:], dtype=np.uint8)
    drawing3 = np.zeros(img.shape[:], dtype=np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    #2.霍夫直线变换
    # 参数1：要检测的二值图（一般是阈值分割或边缘检测后的图）
    # 参数2：距离r的精度，值越大，考虑越多的线
    # 参数3：角度θ的精度，值越小，考虑越多的线
    # 参数4：累加数阈值，值越小，考虑越多的
    lines=cv2.HoughLines(edges,0.8,np.pi/180,90)

    #3.1将检测的线画出来（注意是极坐标的哦）

    for line in lines:
        rho,theta=line[0]
        a=np.cos(theta)
        b=np.sin(theta)
        x0=a*rho
        y0=b*rho

        x1=int(x0+1000*(-b))
        y1=int(y0+1000*(a))
        x2=int(x0-1000*(-b))
        y2=int(y0-1000*(a))

        cv2.line(drawing,(x1,y1),(x2,y2),(0,0,255))



    #3.2统计概率霍夫直线变换

    lines2=cv2.HoughLinesP(edges,0.8,np.pi/180,90,minLineLength=50,maxLineGap=10)
    for l in lines2:
        x1,y1,x2,y2=l[0]
        cv2.line(drawing2,(x1,y1),(x2,y2),(0,255,0),1,lineType=cv2.LINE_AA)



    #霍夫圆变换
    # 参数2：变换方法，一般使用霍夫梯度法，详情：HoughModes
    # 参数3 dp = 1：表示霍夫梯度法中累加器图像的分辨率与原图一致
    # 参数4：两个不同圆圆心的最短距离
    # 参数5：param2跟霍夫直线变换中的累加数阈值一样
    circles=cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,param2=30)
    circles=np.int0(np.around(circles))

    for i in circles[0,:]:
        cv2.circle(drawing3,(i[0],i[1]),i[2],(0,255,0),2)#画出外圆
        cv2.circle(drawing3,(i[0],i[1]),2,(255,0,0),3)#画出圆心



    cv2.imshow("temp", np.hstack((img,drawing,drawing2,drawing3)))
    cv2.waitKey(0)


if __name__ == "__main__":
    f1()
