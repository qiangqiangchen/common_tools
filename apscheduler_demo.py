# -*- coding:utf-8 -*-
import subprocess
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def aps_test(targe):
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),targe)

def remind(targe):
    #subprocess.call("@echo hello")
    os.system("F:\\echo.bat")
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), targe)

def del_aps(targe):
    scheduler.remove_job("interval_task")
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), targe)
scheduler=BlockingScheduler()
"""
trigger有三个参数可设置，分别为：cron/date/interval
cron:表示定时任务
date:表示具体的一次性任务
interval:表示循环任务
"""
scheduler.add_job(func=aps_test,args=("定时任务",),trigger="cron",second="*/5")
scheduler.add_job(func=remind,args=("一次性任务",),next_run_time=datetime.datetime.now()+datetime.timedelta(seconds=3))
scheduler.add_job(func=aps_test,args=("循环任务",),trigger="interval",seconds=3,id="interval_task")
scheduler.start()