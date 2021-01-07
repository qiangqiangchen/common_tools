# -*- coding: utf-8 -*-
"""
绘制
目标：
1.绘制各种几何形状，添加文字
2.OpenCV函数：cv2.line(), cv2.circle(), cv2.rectangle(), cv2.ellipse(), cv2.putText()

绘制形状有一些共同的参数：
img:要绘制形状的图片
color:绘制的颜色
    彩色图就传入BGR 的一组值，如蓝色就是（255,0,0）
    灰度图，传入一个灰度值就行
thickness:线宽，默认为1.对于矩形/圆之类的封闭形状而言，传入-1表示填充形状
"""
import datetime
import math

import numpy as np
import matplotlib.pyplot as plt
import cv2

# 创建一副黑色的图片
img = np.zeros((512, 512, 3), np.uint8)


def draw():
    # 画一条线宽为5的蓝色直线，参数2：起点，参数3：终点，参数4：线条颜色，参数5：线宽
    cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)

    # 画矩形
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    # 画圆,需要制定圆心和半径
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

    # 画椭圆
    # 参数2：椭圆中心(x, y)
    # 参数3：x / y轴的长度
    # 参数4：angle—椭圆的旋转角度
    # 参数5：startAngle—椭圆的起始角度
    # 参数6：endAngle—椭圆的结束角度
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), 3)

    # 画多边形
    pts = np.array([[10, 5], [50, 10], [70, 20], [20, 30]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 255, 255))

    # 添加文字
    # 参数2：要添加的文本
    # 参数3：文字的起始坐标（左下角为起点）
    # 参数4：字体
    # 参数5：文字大小（缩放比例）
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "python", (10, 500), font, 4, (255, 255, 255), 2, lineType=cv2.LINE_AA)

    cv2.imshow("demo", img)
    cv2.waitKey(0)


def clock():
    imgs = np.zeros((550, 450, 3), np.uint8)
    imgs[:] = (255, 255, 255)

    center = (center_x, center_y) = (225, 225)  # 圆心
    margin = 5  # 上下左右边距
    radius = 220  # 圆的半径

    cv2.circle(imgs, center, radius, (0, 0, 0), 3)
    cv2.circle(imgs, center, 8, (0, 0, 0), -1)
    # 秒刻度
    #math.cos()里面传的参数是弧度,弧度计算:角度*pi/180
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


    while(1):
        #拷贝表盘，不然会重叠在一起
        temp=np.copy(imgs)

        #获取系统时间
        now_time=datetime.datetime.now()
        hour,minute,second=now_time.hour,now_time.minute,now_time.second

        #画秒刻度
        #OpenCV中的角度是顺时针计算的，所以需要转化下
        sec_angle=second*6+270 if second <=15 else (second-15)*6

        sec_x=center_x+(radius-margin-40)*math.cos(sec_angle*np.pi/180.0)
        sec_y=center_y+(radius-margin-40)*math.sin(sec_angle*np.pi/180.0)
        cv2.line(temp,center,(int(sec_x),int(sec_y)),(0,0,0),2)

        # 画分刻度
        # OpenCV中的角度是顺时针计算的，所以需要转化下
        min_angle = minute * 6 + 270 if minute <= 15 else (minute - 15) * 6

        min_x = center_x + (radius - margin - 80) * math.cos(min_angle * np.pi / 180.0)
        min_y = center_y + (radius - margin - 80) * math.sin(min_angle * np.pi / 180.0)
        cv2.line(temp, center, (int(min_x), int(min_y)), (0, 0, 0), 4)

        # 画时刻度
        hour_angle = hour * 30 + 270 if hour <= 3 else (hour - 3) * 30
        new_hour_angle=int(hour_angle+minute/60*30)
        hour_x = center_x + (radius - margin - 130) * math.cos(new_hour_angle * np.pi / 180.0)
        hour_y = center_y + (radius - margin - 130) * math.sin(new_hour_angle * np.pi / 180.0)
        cv2.line(temp, center, (int(hour_x), int(hour_y)), (0, 0, 0), 8)


        #写日期
        font=cv2.FONT_HERSHEY_SIMPLEX
        time_str=now_time.strftime("%d/%m/%Y")
        cv2.putText(temp,time_str,(135,500),font,1,(0,0,0),2)

        cv2.imshow("demo", temp)
        if cv2.waitKey(1) == 27:
            break


if __name__ == "__main__":
    clock()
