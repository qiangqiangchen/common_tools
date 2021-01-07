# -*- coding: utf-8 -*-
"""
腐蚀与膨胀
目标：
1.学习膨胀、腐蚀、开运算和闭运算等形态学操作
2.OpenCV函数：cv2.erode(), cv2.dilate(), cv2.morphologyEx()

"""
import cv2
import matplotlib.pyplot as plt

import numpy as np

img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\1556514111.png', 0)
# img = cv2.imread(r"E:\test.png", 0)
#阈值分割，切出头像部分
Roi = img[30:170, 30:250]
ret, mask = cv2.threshold(Roi, 150, 255, cv2.THRESH_BINARY)
#平滑图像
median=cv2.medianBlur(mask,5)
median=mask



def f1():
    """
    腐蚀
    :return:
    """
    temp = cv2.bitwise_not(median)
    kernel1=np.ones((10,10),np.uint8)
    #腐蚀的效果是把图片”变瘦”，其原理是在原图的小区域内取局部最小值
    erosion=cv2.erode(temp,kernel1)
    #膨胀与腐蚀相反，取的是局部最大值，效果是把图片”变胖”
    dilation=cv2.dilate(temp,kernel1)

    cv2.imshow("img", np.hstack((temp,erosion,dilation)))
    cv2.waitKey(0)

def f2():
    """
    开闭运算
    :return:
    """
    temp=cv2.bitwise_not(median)
    kernel1=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

    #先腐蚀后膨胀叫开运算（因为先腐蚀会分开物体，这样容易记住），其作用是：分离物体，消除小区域。
    opening=cv2.morphologyEx(temp,cv2.MORPH_OPEN,kernel1)
    #闭运算则相反：先膨胀后腐蚀（先膨胀会使白色的部分扩张，以至于消除 /“闭合”物体里面的小黑洞，所以叫闭运算）
    closing=cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel1)
    cv2.imshow("img", np.hstack((temp, opening,closing)))
    cv2.waitKey(0)

if __name__ == "__main__":
    f2()
