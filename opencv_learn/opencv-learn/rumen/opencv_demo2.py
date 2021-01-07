# -*- coding: utf-8 -*-
"""
视频相关操作
目标：
1.打开摄像头并拍照
2.播放本地视频，录制视频
2.使用到的函数：cv2.VideoCapture(),cv2.VideoWriter()

打开摄像头或者播放本地视频
cv2.VideoCapture()参数:数字表示摄像头编号，第一个为0，本地视频传入视频路径


保存视频
cv2.VideoWriter（）参数：1.输出的文件名，2.编码方式FourCC码，3.帧率FPS ，要保存的分辨率大小


"""

import cv2

# 读取视频，逐帧转换为黑白，播放
def play():
    capture = cv2.VideoCapture(r"F:\BVR_2020_09_30_18_03_49.mp4")
    index=0
    while(capture.isOpened()):
        ret,frame=capture.read()
        if ret:
            #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imwrite(r'F:\dd\%04d.jpg'%index,frame)
            index+=1
            #if cv2.waitKey(25)==ord('q'):
            #    break
        else:
            break

#把视频转换为360*640分辨率的
def write_video():
    f = cv2.VideoWriter_fourcc(*'mp4v')
    outfile = cv2.VideoWriter('out.mp4', f, 30, (360, 640))
    capture = cv2.VideoCapture(r"..\image\demo.mp4")
    while(capture.isOpened()):
        ret,frame=capture.read()
        if not ret:
            break
        new_gray=cv2.resize(frame,(360,640),interpolation=cv2.INTER_AREA)
        outfile.write(new_gray)





if __name__ == "__main__":
    play()

