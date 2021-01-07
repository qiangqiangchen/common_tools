# -*- coding: utf-8 -*-
"""
基本操作
目标：
1.加载图片，显示图片，保存图片
2.使用到的函数：cv2.imread(),cv2.imshow(),cv2.imwrite()

加载图片
imread()参数:1.图片路径，2.读入方式
cv2.IMREAD_COLOR：彩色图，默认值为（1）
cv2.IMREAD_GRAYSCALE：灰度图，默认值(0)
cv2.IMREAD_UNCHANGED：包含透明通道的彩色图(-1)

显示图片
cv2.imshow（）参数：1.窗口的名字，2.要显示的名字

"""

import cv2

if __name__ == "__main__":
    # 加载图片
    img = cv2.imread(r"..\image\bage.jpeg", 0)
    img2 = cv2.imread(r"..\image\fadou.jpg", 1)

    # 显示图片
    cv2.imshow('bage', img)

    # 新建一个窗口，参数设置为窗口大小可调，默认参数为cv2.WINDOW_NORMAL,表示窗口大小自适应图片
    cv2.namedWindow("fadou", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("fadou", 600, 450)
    cv2.imshow('fadou', img2)

    # 程序暂停，参数为等待时间，0为一直等待
    cv2.waitKey(0)

    # 保存图片
    # cv2.imwrite(r'..\image\bage_grayscale.jpg',img)
