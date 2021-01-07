# -*- coding: utf-8 -*-
"""
亮度与对比度
目标：
1.亮度调整是将图像像素的强度整体变大/变小，对比度调整指的是图像暗处的像素强度变低，亮出的变高，从而拓宽某个区域内的显示精度。
2.OpenCV函数：cv2.add(), cv2.addWeighted(), cv2.bitwise_and()

"""
import cv2

import numpy as np



def f1():
    """

    :return:
    """
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\bage.jpeg')
    res = np.uint8(np.clip((img*0.3+10),0,255))
    tmp=np.hstack((img,res))# 两张图片横向合并（便于对比显示）
    cv2.imshow("test2", tmp)
    cv2.waitKey(0)



def f2():
    def nothing(x):
        pass

    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\sudoku.jpg')

    cv2.namedWindow('image')

    cv2.createTrackbar('duibidu', 'image', 1, 300, nothing)
    cv2.createTrackbar('laingdu', 'image', 1, 100, nothing)

    while (1):
        r = cv2.getTrackbarPos('duibidu', 'image')
        g = cv2.getTrackbarPos('laingdu', 'image')

        temp = np.uint8(np.clip((img*r*0.001+g), 0, 255))
        cv2.imshow('image', temp)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


if __name__=="__main__":
    f2()


