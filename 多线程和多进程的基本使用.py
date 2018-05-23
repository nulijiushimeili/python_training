from threading import Thread
import time


def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1


# # 使用单线程
# start_time = time.time()
# my_counter()
# end_time = time.time()
# print("Total time:{}".format(end_time - start_time))
# # Total time:13.010770797729492


# # 启用两个线程执行任务
# start_time = time.time()
# t1 = Thread(target=my_counter)
# t2 = Thread(target=my_counter)
# t1.start()
# t2.start()
# end_time = time.time()
# print("Total time:{}".format(end_time - start_time))
# # Total time:0.0244140625

# -------------------------------------------------------
# multiprocessing是跨平台版本的多进程模块
# 它提供了一个Process类代表一个进程对象
from multiprocessing import Process


def f(n):
    time.sleep(1)
    print(n * n)


# 使用多进程执行,不到一秒钟就可以执行完成
if __name__ == "__main__":
    for i in range(10):
        p = Process(target=f, args=[i, ])
        p.start()

# # 使用单进程执行,需要大约10秒中才能执行完成
# if __name__ == "__main__":
#     for i in range(10):
#         f(i)
