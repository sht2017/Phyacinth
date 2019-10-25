#from multiprocessing import Process, Queue
import multiprocessing
import os, time, random

# 写数据进程执行的代码:
def a(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def b(q):
    while True:
        value = q.get(True)
        print(value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    A = multiprocessing.Queue()
    pw = multiprocessing.Process(target=a, args=(A,))
    print(A,)
    pr = multiprocessing.Process(target=b, args=(A,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    print(A.get(True))
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()