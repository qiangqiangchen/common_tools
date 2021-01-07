# -*- coding:utf-8 -*-
import time
from multiprocessing import Queue
from multiprocessing.managers import BaseManager


class Slave:
    def __init__(self):
        # 派发出去的作业队列
        self.dispatched_job_queue = Queue()
        # 完成的作业队列
        self.finish_job_queue = Queue()
    def start(self):
        # 把派发作业队列和完成作业队列注册到网络上
        BaseManager.register('get_dispatched_job_queue')
        BaseManager.register('get_finish_job_queue')

        #连接到master
        server='127.0.0.1'
        print('Connect to server %s...'%server)
        manager=BaseManager(address=(server,5001),authkey=b'jobs')
        manager.connect()

        #使用上面注册的方法获取队列
        dispatched_jobs=manager.get_dispatched_job_queue()
        finish_jobs=manager.get_finish_job_queue()

        #运行作业并返回结果，这里只是模拟作业运行，所以返回的是接收到的作业
        while True:
            job=dispatched_jobs.get(timeout=1)
            print('Run job: %s ' % job)
            time.sleep(1)
            finish_jobs.put(job*2)

if __name__ == '__main__':
    slave=Slave()
    slave.start()