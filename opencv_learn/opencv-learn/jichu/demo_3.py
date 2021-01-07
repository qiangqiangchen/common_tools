# -*- coding: utf-8 -*-
"""
平滑图像
目标：
1.模糊/平滑图片来消除图片噪声
2.OpenCV函数：cv2.add(), cv2.addWeighted(), cv2.bitwise_and()

"""
import cv2
import matplotlib.pyplot as plt

import numpy as np



def f1():
    """

    :return:
    """
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\small.jpg',0)

    name=["old","blur","boxFilter","GaussianBlur","medianBlur","bilateralFilter"]

    #均值滤波
    blur=cv2.blur(img,(3,3))

    #方框滤波
    blur_1=cv2.boxFilter(img,-1,(3,3),normalize=True)

    #高斯滤波
    gaussian=cv2.GaussianBlur(img,(5,5),1)

    #中值滤波
    median=cv2.medianBlur(img,5)

    #双边滤波
    blur_2=cv2.bilateralFilter(img,9,75,75)

    imgs=[img,blur,blur_1,gaussian,median,blur_2]


    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(imgs[i], 'gray')
        plt.title(name[i], fontsize=8)
        plt.xticks([]), plt.yticks([])
    plt.show()


if __name__=="__main__":
    f1()


