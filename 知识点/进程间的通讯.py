# Queue是多进程--安全--的队列,可以使用Queue实现多进程之间的数据通讯
from multiprocessing import Process, Queue
import time


def write(q):
    for i in ["A", "B", "C", "D", "E", "F"]:
        print("Put {} to queue".format(i))
        q.put(i)
        time.sleep(0.5)


def read(q):
    while (True):
        v = q.get(True)
        print("Get {} from queue".format(v))


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pr.join()
    pr.terminate()

