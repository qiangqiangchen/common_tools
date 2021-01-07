# -*- coding: utf-8 -*-
"""
车道检测
目标：实现车道检测

1.灰度化
2.高斯模糊
3.canny边缘检测
4.不规则ROI区域截取
5.霍夫直线检测
6.车道计算
"""

import cv2

import numpy as np

# 高斯滤波核大小
blur_ksize = 5
# Canny边缘检测高低阈值
canny_lth = 50
canny_hth = 150

def roi_mask(img,corner_points):
    #创建掩膜
    mask=np.zeros_like(img)
    cv2.fillPoly(mask,corner_points,255)
    masked_img=cv2.bitwise_and(img,mask)
    return masked_img

def f1():
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\test_pictures\lane.jpg')
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    blur_gray=cv2.GaussianBlur(gray,(blur_ksize,blur_ksize),1)
    edges=cv2.Canny(blur_gray,canny_lth,canny_hth)

    rows,cols=edges.shape

    points=np.array([[(0,rows),(460,325),(520,325),(cols,rows)]])
    roi_edges=roi_mask(edges,points)

    cv2.imshow("temp",roi_edges)
    cv2.waitKey(0)


def f2():
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\watch.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
    cv2.imshow("temp", th)
    cv2.waitKey(0)

def f3():
    img=np.ones((1080,1920),np.uint8)
    cv2.imshow("temp", img)
    cv2.imwrite("E:\one.jpg",img)
    cv2.waitKey(0)
if __name__=="__main__":
    f3()