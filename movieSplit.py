import cv2
import os
import numpy as np
from skimage.measure import compare_ssim
import time


def movie_caption_extract(movie_path):
    split_path = r'F:\movie\split'
    if not os.path.exists(split_path):
        os.makedirs(split_path)
    capture = cv2.VideoCapture(movie_path)
    tmp = np.zeros((98, 1280), np.uint8)
    black_img = np.zeros((98, 1280), np.uint8)
    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            height, width = gray.shape[:2]
            caption = gray[int(height * 0.84):int(height * 0.98), 0:width]
            ret, th = cv2.threshold(caption, 235, 255, cv2.THRESH_BINARY)
            kernel1 = np.ones((25, 25), np.uint8)
            # 膨胀
            dilation = cv2.dilate(th, kernel1)
            kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))
            opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel2)
            closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel2)
            if comp_img(black_img, closing, 0.95):
                # print('图片为纯黑')
                pass
            elif comp_img(tmp, closing, 0.9):
                # print('与上一张相同')
                pass
            else:
                tmp = closing
                print('图片保存')
                cv2.imwrite(r'F:\movie\split\{}.jpg'.format(int(time.time() * 1000)), frame)

            # cv2.imshow('video_caption', th)
            # cv2.imshow('dilation', dilation)
            # cv2.imshow('opening', opening)

            # cv2.imshow('closing', closing)
            # if cv2.waitKey(10) == ord('q'):
            #     break
        else:
            break


def movie_caption_extract2(movie_path):
    split_path = r'F:\movie\split'
    if not os.path.exists(split_path):
        os.makedirs(split_path)
    capture = cv2.VideoCapture(movie_path)
    tmp = 0
    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret:
            height, width = frame.shape[:2]
            caption = frame[int(height * 0.84):int(height * 0.98), 0:width]
            caption_gray = cv2.cvtColor(caption, cv2.COLOR_BGR2GRAY)
            ret, th = cv2.threshold(caption_gray, 245, 255, cv2.THRESH_BINARY)
            # 膨胀
            kernel1 = np.ones((25, 25), np.uint8)
            dilation = cv2.dilate(th, kernel1)
            kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))
            opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel2)
            closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel2)

            image, contours, hierarchy = cv2.findContours(closing, 3, 2)
            if len(contours) > 0:
                length = cv2.arcLength(contours[0], True)
                if length > 430:
                    cv2.drawContours(caption, contours, 0, (0, 0, 255), 2)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame, str(int(length)), (50, 50), font, 0.6, (0, 0, 255), 2, lineType=cv2.LINE_AA)
                    if abs(length-tmp)>10:
                        tmp=length
                        cv2.imwrite(r'F:\movie\split\{}.jpg'.format(int(time.time() * 1000)), frame)

                # elif 400 < length < 430:
                #     cv2.drawContours(caption, contours, 0, (0, 255, 0), 2)
                #     font=cv2.FONT_HERSHEY_SIMPLEX
                #     cv2.putText(frame,str(int(length)),(50,50),font,0.6,(0,0,255),2,lineType=cv2.LINE_AA)
                #
                #     cv2.imwrite(r'F:\movie\split\{}.jpg'.format(int(time.time() * 1000)), frame)
            # cv2.imshow('caption', caption)
            # cv2.imshow('caption', caption)
            # cv2.imshow('video_caption', th)
            # cv2.imshow('dilation', closing)
            # if cv2.waitKey(10) == ord('q'):
            #     break
        else:
            break


def comp_img(img, img2, template):
    score, diff = compare_ssim(img, img2, full=True)
    if score >= template:
        return True
    return False


if __name__ == '__main__':
    in_movie_name = r'F:\movie\new.mp4'
    out_movie_name = r'E:\Temp\movie_temp\new2.mp4'
    frame_img = r'E:\Temp\frame.jpg'
    movie_dir = r'E:\Temp\movie_temp'
    movie_caption_extract2(in_movie_name)
    # print(int(time.time()*1000))
    print('succeed')
