import numpy as np

# 生成0-1之间的随机数
print(np.random.rand())
# 生成3行4列的随机数矩阵
print(np.random.rand(3, 4))
# 生成4个元素的数组
print(np.random.rand(4))

# 生成0-2之间的数
print(np.random.randint(2))
# 0-3之间的随机数组成的长度为5 的数组
print(np.random.randint(3, size=5))
# 一个元素的数组,取值为5-10的随机整数
print(np.random.randint(5, 10))
# 5-10之间的随机整数组成的5个元素长度的数组
print(np.random.randint(5, 10, size=5))
# 2*3的矩阵,区间为2-5之间,不包含5
print(np.random.randint(2, 5, (2, 3)))

# 产生正太分布的样本值(均值为0,标准差为1)
print(np.random.randn(10))

# np.random.seed(),设置随机数种子,每次生成相同的随机数
# 配合其他方法使用,一定作用域内有效
for i in range(5):
    np.random.seed(3)
    print(np.random.random())

# shuffle()将一个队列的顺序打乱
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)

# 产生均匀分布的值
print(np.random.rand(10))

# 产生高斯分布的值
# numpy.random.normal(loc=0.0, scale=1.0, size=None)
# 参数的意义为：
# 　　loc:float
# 　　概率分布的均值，对应着整个分布的中心center
# 　　scale:float
# 　　概率分布的标准差，对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高
# 　　size:int or tuple of ints
# 　　输出的shape，默认为None，只输出一个值
# 　　我们更经常会用到np.random.randn(size)所谓标准正太分布（μ=0, σ=1），对应于np.random.normal(loc=0, scale=1, size)
print(np.random.normal(loc=0, scale=1, size=10))

# 产生二项分布的样本值
print(np.random.binomial(10, 0.5, size=2))
# https://blog.csdn.net/lanchunhui/article/details/50172659

# 随机漫步
# python的实现
import random

times = 1000
position = 0
walk = [position]
for i in range(1000):
    rd = random.randint(0, 1)
    step = 1 if rd == 1 else -1
    position += step
    walk.append(position)
# print(walk)

# numpy的实现
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum()
print(walks)

# ----------------------------------------------

# 线性代数的计算函数
# diag()  # 以一维数组的形势返回方阵的对角线,也可以将以为数组转换成对角方阵
# dot()  # 矩阵乘法
# trace()  # 计算对角元素的和
# det()  # 计算矩阵的行列式
# eig()  # 计算方阵的本征值和本征向量
# inv()  # 矩阵求逆
# pinv()  # 计算矩阵的Moore-Penrose违逆
# qr()  # 计算QR分解
# svd()  # 计算奇异值分解
# solve()  # 解线性方程组Ax=b,其中A是一个方阵
# lstsq()  # 计算Ax=b的最小二乘解
