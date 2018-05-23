# 进程池Pool
# --用于批量创建子进程,可以灵活控制子进程的数量
from multiprocessing import Pool
import time


def f(x):
    print(x * x)
    time.sleep(2)
    return x * x


if __name__ == "__main__":
    # 定义进程的个数
    pool = Pool(processes=5)
    res_list = []

    for i in range(10):
        # 以异步并行的方式启动进程,如果要同步等待的方式
        # 可以在每次启动进程之后调用res.get()方法,也可以使用Pool.apply
        # Pool.apply_async(函数名,参数列表)
        res = pool.apply_async(f, [i, ])
        print("-----:{}".format(i))
        res_list.append(res)
    pool.close()
    pool.join()
    for r in res_list:
        print("result", r.get(timeout=5))
