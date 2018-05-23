# 在一般情况下,多个进程的内存资源是相互独立的,
# 而多进程可以共享同一个进程中的内存资源
# 创建进程的速度比较慢,线程的启动速度则很快
from multiprocessing import Process
import threading
import time

# 设置线程锁
lock = threading.Lock()


# 多线程或多进程执行的函数
def run(info_list, n):
    # 获取锁
    lock.acquire()
    info_list.append(n)
    # 释放锁
    lock.release()
    print("{}".format(info_list))


if __name__ == "__main__":
    info = []
    for i in range(10):
        # target是子进程的函数,args是该函数的参数
        p = Process(target=run, args=[info, i])
        p.start()
        p.join()
    time.sleep(2)  # 这里是为了输出整齐,让主进程等一下字进程
    print("-------------------华丽的分割线----------------")
    for i in range(10):
        t = threading.Thread(target=run, args=[info, i])
        t.start()
        t.join()

