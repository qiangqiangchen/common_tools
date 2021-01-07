# -*- coding: utf-8 -*-
"""
绘制
目标：
1.画一个时钟
2.使用鼠标绘图
"""
import datetime
import math

import numpy as np
import matplotlib.pyplot as plt
import cv2


def clock():
    imgs = np.zeros((550, 450, 3), np.uint8)
    imgs[:] = (255, 255, 255)

    center = (center_x, center_y) = (225, 225)  # 圆心
    margin = 5  # 上下左右边距
    radius = 220  # 圆的半径

    cv2.circle(imgs, center, radius, (0, 0, 0), 3)
    cv2.circle(imgs, center, 8, (0, 0, 0), -1)
    # 秒刻度
    # math.cos()里面传的参数是弧度,弧度计算:角度*pi/180
    wai = [(int(center_x + (radius - margin) * math.cos(i * 6 * np.pi / 180)),
            int(center_x + (radius - margin) * math.sin(i * 6 * np.pi / 180))) for i in range(60)]
    nei = [(int(center_x + (radius - 15) * math.cos(i * 6 * np.pi / 180)),
            int(center_x + (radius - 15) * math.sin(i * 6 * np.pi / 180))) for i in range(60)]
    for i in range(60):
        cv2.line(imgs, wai[i], nei[i], (0, 0, 0), 2)

    wai_1 = [(int(center_x + (radius - margin) * math.cos(i * 30 * np.pi / 180)),
              int(center_x + (radius - margin) * math.sin(i * 30 * np.pi / 180))) for i in range(12)]
    nei_1 = [(int(center_x + (radius - 25) * math.cos(i * 30 * np.pi / 180)),
              int(center_x + (radius - 25) * math.sin(i * 30 * np.pi / 180))) for i in range(12)]
    for i in range(12):
        cv2.line(imgs, wai_1[i], nei_1[i], (0, 0, 0), 5)

    while (1):
        # 拷贝表盘，不然会重叠在一起
        temp = np.copy(imgs)

        # 获取系统时间
        now_time = datetime.datetime.now()
        hour, minute, second = now_time.hour, now_time.minute, now_time.second

        # 画秒刻度
        # OpenCV中的角度是顺时针计算的，所以需要转化下
        sec_angle = second * 6 + 270 if second <= 15 else (second - 15) * 6

        sec_x = center_x + (radius - margin - 40) * math.cos(sec_angle * np.pi / 180.0)
        sec_y = center_y + (radius - margin - 40) * math.sin(sec_angle * np.pi / 180.0)
        cv2.line(temp, center, (int(sec_x), int(sec_y)), (0, 0, 0), 2)

        # 画分刻度
        # OpenCV中的角度是顺时针计算的，所以需要转化下
        min_angle = minute * 6 + 270 if minute <= 15 else (minute - 15) * 6

        min_x = center_x + (radius - margin - 80) * math.cos(min_angle * np.pi / 180.0)
        min_y = center_y + (radius - margin - 80) * math.sin(min_angle * np.pi / 180.0)
        cv2.line(temp, center, (int(min_x), int(min_y)), (0, 0, 0), 4)

        # 画时刻度
        hour_angle = hour * 30 + 270 if hour <= 3 else (hour - 3) * 30
        new_hour_angle = int(hour_angle + minute / 60 * 30)
        hour_x = center_x + (radius - margin - 130) * math.cos(new_hour_angle * np.pi / 180.0)
        hour_y = center_y + (radius - margin - 130) * math.sin(new_hour_angle * np.pi / 180.0)
        cv2.line(temp, center, (int(hour_x), int(hour_y)), (0, 0, 0), 8)

        # 写日期
        font = cv2.FONT_HERSHEY_SIMPLEX
        time_str = now_time.strftime("%d/%m/%Y")
        cv2.putText(temp, time_str, (135, 500), font, 1, (0, 0, 0), 2)

        cv2.imshow("demo", temp)
        if cv2.waitKey(1) == 27:
            break


# 获取鼠标的事件
img = np.zeros((512, 512, 3), np.uint8)
drawing = False
start = (-1, -1)


def mouse_ecent(event, x, y, flags, param):
    global start, drawing
    temp=()
    if event == cv2.EVENT_LBUTTONDOWN:
        print("mouse left button down:({},{}".format(x, y))
        drawing = True
        start = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        print("mouse left button up:({},{})".format(x, y))
        drawing = False
        cv2.line(img, start, (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            start=(x,y)
            # cv2.rectangle(img, start, (x, y), (0, 255, 0), -1)
            cv2.line(img,start,(x,y),(0,255,0),2)
            print("mouse left button move:({},{})".format(x, y))


def draw():
    cv2.namedWindow("image")
    cv2.setMouseCallback('image', mouse_ecent)
    while (True):
        cv2.imshow('image', img)
        if cv2.waitKey(100) == 27:
            break


if __name__ == "__main__":
    draw()
