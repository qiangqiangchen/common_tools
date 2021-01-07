# -*- coding:utf-8 -*-
from multiprocessing import Queue
from multiprocessing.managers import BaseManager

class Master:
    def __init__(self):
        # 派发出去的作业队列
        self.dispatched_job_queue = Queue()
        # 完成的作业队列
        self.finish_job_queue = Queue()

    def get_dispatched_job_queue(self):
        return self.dispatched_job_queue

    def get_finish_job_queue(self):
        return self.finish_job_queue

    def stsrt(self):
        # 把派发作业队列和完成作业队列注册到网络上
        BaseManager.register('get_dispatched_job_queue', callable=self.get_dispatched_job_queue)
        BaseManager.register('get_finish_job_queue', callable=self.get_finish_job_queue)

        # 监听端口和启动服务
        manager = BaseManager(address=('127.0.0.1', 5001), authkey=bytes('jobs', encoding='utf-8'))
        manager.start()

        # 使用上面注册的方法获取队列
        dispatched_jobs = manager.get_dispatched_job_queue()
        finished_jobs = manager.get_finish_job_queue()

        # 一次派发10个作业，等到10个作业都运行完成，再继续派发10个作业
        job_id = 0
        while True:
            for i in range(0, 10):

                print('Dispatch job:%d' %i)
                dispatched_jobs.put(i)
            while not dispatched_jobs.empty():
                job = finished_jobs.get(60)
                print('Finish Job:%s ' % int(job))
        manager.shutdown()

if __name__ == '__main__':
    master = Master()
    master.stsrt()
