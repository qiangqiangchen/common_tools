import cv2


def movie_caption_extract():
    movie_path = r'F:\movie\xinling.mp4'
    split_path = r'F:\movie\split'
    capture = cv2.VideoCapture(movie_path)
    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            height, width = gray.shape[:2]
            caption = gray[int(height * 0.83):int(height * 0.98), 0:width]
            cv2.imshow('video_caption', caption)
            cv2.imshow('video', gray)
            if cv2.waitKey(10) == ord('q'):
                break
        else:
            break

def timeformat(t):
    if t <60:
        h=0
        m=0
        s=t
    else:
        h=int(t/3600)
        m=int((t-3600*h)/60)
        s=t%60
    print("{}:{}:{}".format(h,m,s))
    return "{}:{}:{}".format(h,m,s)

def movie_split(movie_path,out_movie_path,start_time,end_time):
    if isinstance(start_time,int) and  isinstance(end_time,int):
        start_time=timeformat(start_time)
        end_time=timeformat(end_time)
        cmd="ffmpeg -ss {} -t {} -i {} -vcodec copy -acodec copy {}".format(start_time,end_time,movie_path,out_movie_path)
        return True
    else:
        return False



if __name__ == '__main__':
    pass
