import ffmpeg
import os


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

def create_movie_list(movie_dir):
    list=os.listdir(movie_dir)
    movie_list= os.path.join(movie_dir,'movie_list.txt')
    with open(movie_list,'w') as f:
        for i in list:
            if i.endswith('.mp4'):
                f.write("file '{}'\n".format(os.path.join(movie_dir,i)))
    return movie_list

def movie_cut(movie_path,out_movie_path,start_time,duration):
    out, err = (
        ffmpeg.input(movie_path, ss=start_time, t=duration).output(out_movie_path, codec="copy").run(quiet=False, overwrite_output=True)
    )
    if out == b'':
        print('do nothing')


def movie_concat(movie_dir, out_movie_path):
    try:
        out, err = (
            ffmpeg
                .input(create_movie_list(movie_dir),f='concat',safe=0)
                .output(out_movie_path, c="copy")
                .run(quiet=False, overwrite_output=True)
        )
        return True
        if out == b'':
            print('do nothing')
            return False
    except Exception as e:
        print(e)
        return False



def get_movie_info(movie_path):
    info = ffmpeg.probe(movie_path)
    print(type(info))
    for i in info:
        print(i)

def get_frame_by_time(movie_path,frame_img,time):
    out,err=(
        ffmpeg
            .input(movie_path, ss=time)
            .output(frame_img, vframes='1', f='image2')
            .run(quiet=False, overwrite_output=True)
    )
    if out == b'':
        print('do noting')


if __name__ == '__main__':
    in_movie_name=r'E:\Temp\xinling.mp4'
    out_movie_name=r'E:\Temp\concat.mp4'
    frame_img=r'E:\Temp\frame.jpg'
    movie_dir=r'E:\Temp\movie_temp'
    # movie_cut(in_movie_name,out_movie_name,300,60)
    # movie_caption_extract(out_movie_name)
    # get_movie_info(out_movie_name)
    # get_frame_by_time(out_movie_name,frame_img,3)
    # create_movie_list(movie_dir)
    movie_concat(movie_dir,out_movie_name)