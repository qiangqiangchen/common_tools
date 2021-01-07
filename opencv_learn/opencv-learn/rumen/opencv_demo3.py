# -*- coding: utf-8 -*-
"""
图片基本操作
目标：
1.访问和修改图片像素点的值
2.获取图片的宽、高、通道数等属相
3.了解感兴趣区域的ROI
4.分离和合并图像通道

"""

import cv2


def edit():
    # 对于彩色图，结果是B，G，R三个值的列表，对于灰度图或者单通通道，只有一个值
    img = cv2.imread(r"..\image\bage.jpeg")
    px = img[100, 90]
    print(px)

    # 只获取蓝色blue通道的值
    px_blue = img[100, 90, 0]
    print(px_blue)

    # 修改像素值
    img[100, 90] = [255, 255, 255]
    print(img[100, 90])


def getshape():
    img = cv2.imread(r'E:\pycharmproject\pythonlearn\image\sipo.png')
    height, width, channels = img.shape

    print("height:{},width:{},channels:{}".format(height, width, channels))
    print("图像的数据类型：{}".format(img.dtype))
    print("图像的总像素数：{}".format(img.size))


def getROI():
    # ROI：region of interest  感兴趣区域
    img = cv2.imread(r'F:\20191210152119.JPG')
    height, width=img.shape[:2]
    face = img[int(height*0.8):height, 0:width]
    img2gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("face", img2gray)
    cv2.waitKey(0)


def split_and_merga():
    img = cv2.imread(r"..\image\bage.jpeg")
    # 分割和合并可以使用cv2.split()和cv2.merge()方法
    # b,g,r=cv2.split(img)
    # img=cv2.merge((b,g,r))

    # 分割图片，split()函数比较耗时，更高效的方式是用numpy中的索引，如提取B通道：
    b = img[:, :, 0]
    g=img[:, :,1]
    r=img[:, :, 2]
    new_img=cv2.merge((b,g,r))
    cv2.imshow('blue', new_img)
    cv2.waitKey(0)


if __name__ == "__main__":
    # getshape()
    getROI()
