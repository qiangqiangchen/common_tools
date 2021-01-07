# -*- coding:utf-8 -*-
import time

import requests
import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import *
from common.Logger import Logger

Logger = Logger(logger="download_tool").getlog()
base_dir = r"E:\ddd"


def download(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        resource_name = url.split("/")[-1]
        resource_leng = int(response.headers['Content-Length'])
        with tqdm(total=resource_leng) as pbar:
            pbar.set_description("current download file is {}".format(resource_name))
            with open(os.path.join(base_dir, resource_name), 'wb') as f:
                for chunk in response.iter_content(512):
                    f.write(chunk)
                    pbar.update(512)
    else:
        print("url is disable")


def download2(url, name):
    Logger.info('curretn download {}:{}'.format(url, name))
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        resource_leng = int(response.headers['Content-Length'])
        Logger.info('downloading is {}...'.format(name))
        with open(name, 'wb') as f:
            for chunk in response.iter_content(512):
                f.write(chunk)
        Logger.info(' {} download finish.'.format(name))
    else:
        Logger.error("url is disable:{}:{}".format(url, name))


def muiltDownload(urls, base_path):
    base_path = base_path
    index = 1000
    with ThreadPoolExecutor(3) as executor:
        for url in urls:
            executor.submit(download2, url, os.path.join(base_path, str(index) + '.jpg'))
            index += 1


if __name__ == "__main__":
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    urls = [
        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1576674335439&di=648b0a0c5586a7defc9182776e7c2982&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn06%2F100%2Fw540h360%2F20180407%2Fe81c-fytnfyn9849464.jpg',
        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1576674370379&di=c921be8786fe88eb53feb0e410c1a666&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn%2F20171116%2Fad7d-fynwxum1427222.jpg',
        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1576674391863&di=c9f11a493bd033bb6890006e2b3c6930&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn16%2F40%2Fw480h360%2F20180923%2F37d3-hikxxna7993195.jpg',
        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1576674411372&di=6ff285fde7d778fa7c2137d5f7fdc621&imgtype=0&src=http%3A%2F%2Fimg.jpjww.com%2Fimg%2F9e116c4234bacb19.jpg',
        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1576674423247&di=92cfca94a944e0bacc52dc580c3dc759&imgtype=0&src=http%3A%2F%2Fimg0.d17.cc%2Ffile%2Fupload%2F201405%2F06%2F11-45-26-51-171608.jpg',
        'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1755862171,2871496445&fm=26&gp=0.jpg']

    # muiltDownload(urls)
    print('<=+=>'.join(urls))

    ""
