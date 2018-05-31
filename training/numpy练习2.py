import numpy as np

# 将条件逻辑表述为数组运算
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
# 根据cond的值选取xarr和yarr中的值,
# 如果True,从xarr中选取,否则从yarr中选取
# 使用列表推导式如下
result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]
print(result)
# 实现上述的功能效率并不是很高,而且写起来也费事
# 下面是numpy的写法,实现同样的功能显得十分简洁
res = np.where(cond, xarr, yarr)
print(res)
# np.where()的第二个参数和第三个参数不必是数组,它们可以是标量值

# 假设有一个随机数据组成的矩阵,将>0的数换成2,<0的值换成-2
# 使用np.where()会非常简单
arr = np.random.rand(4, 4)
print(arr)
res = np.where(arr > 0.5, 2, -2)
print(res)
# 只转换满足条件的值
res = np.where(arr > 0.5, 5, arr)
print(res)

# np.where()方法的高级应用
# 先看看python是怎么写的
cond1 = np.array([True, False, False, True, True, False])
cond2 = np.array([True, False, True, True, True, False])
result = []
for i in range(len(cond1)):
    if cond1[i] and cond2[i]:
        result.append(1)
    elif cond1[i]:
        result.append(2)
    elif cond2[i]:
        result.append(3)
    else:
        result.append(4)
print(result)
# 如果使用numpy.where()
res = np.where(cond1 & cond2, 1,
               np.where(cond1, 2,
                        np.where(cond2, 3, 4)))
print(res)

# 数学和统计方法
arr = np.random.randn(5, 4)  # 正太分布数据
print(arr)
print(arr.mean())
print(np.mean(arr))
print(np.sum(arr))
# mean(),sum()可以接受一个参数axis(用于计算该轴上的统计值)
print(arr.mean(axis=1))
print(arr.sum(0))
# 得到的结果是以为数组

arr = np.arange(1, 6)
print(arr)
# 方差
print(np.var(arr))
# 标准差
print(np.std(arr))
# 返回最大值和最小值的位置
print(np.argmax(arr))
print(np.argmin(arr))
# 得到一个累加的数组
print(np.cumsum(arr))
# 累积
print(np.prod(arr))

# 用于布尔型数组的方法
# 布尔值会被强制转换成0 或 1
arr = np.random.randn(100)
print(arr)
# 计算所有正数的和
print((arr > 0).sum())
# any(),测试数组中是否存在一个或多个True,
# all(),检查数组中的值是否都为True
bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())

# 排序
arr = np.random.randn(8)
print(arr)
arr.sort()
print(arr)

# 多维数组的排序
arr = np.random.randn(4, 3)
print(arr)
# 对每一行的值进行排序
arr.sort(1)
print(arr)

arr = np.random.randn(1000)
arr.sort()
# 排序后选择特定位置的值
print(arr[int(0.05 * len(arr))])  # 5%分位数

# 返回集合中出现过的值,并且是经过排序后得到的值
names = np.array(["Hello", "Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
# 可以理解为返回俩集合的并集
print(np.unique(names))
nums = np.array([12, 2, 2, 2, 3, 3, 566, 7])
print(np.unique(nums))
# 使用python的方法实现
res = list(set(nums))
print(res)

# 找出一个数组的元素是否在另一个数组中出现过
values = np.array([1, 2, 3, 4, 5, 6])
# 第二个集合是否包含于第一个集合
res = np.in1d(values, [3, 4, 9])
# 返回的是布尔值的集合
print(res)
# 返回集合的差集
print(np.setdiff1d(values, [3, 4]))

# 将数组以二进制的方式保存到磁盘
# arr = np.arange(10)
# np.save("array_file",arr)
# 读取保存到磁盘的数据
arr = np.load("array_file.npy")
print(arr)

# 使用np.savez()将多个数组保存到一个压缩文件中
# np.savez("arr_z.npz",a=arr,b=arr)
# 加载.npz文件时,得到一个字典对象,这个对象会对各个数组进行延迟加载
# arch = np.load("arr_z.npz")
# print(arch["b"])

# 一次模拟多个随机漫步
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))  # 0 或 1
steps = np.where(draws > 0, 1, -1)
# 对行的值累加求和
walks = steps.cumsum(1)
print(walks)
print(walks.max())
print(walks.min())
# 返回绝对值是否超过30的数
hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum())

crossing_time = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_time.mean())
