import numpy as np

# 生成0-1之间的随机数
print(np.random.rand())
# 生成3行4列的随机数矩阵
print(np.random.rand(3,4))
# 生成4个元素的数组
print(np.random.rand(4))

# 生成0-2之间的数
print(np.random.randint(2))
# 0-3之间的随机数组成的长度为5 的数组
print(np.random.randint(3, size = 5))
# 一个元素的数组,取值为5-10的随机整数
print(np.random.randint(5, 10))
# 5-10之间的随机整数组成的5个元素长度的数组
print(np.random.randint(5, 10,size=5))
# 2*3的矩阵,区间为2-5之间,不包含5
print(np.random.randint(2,5,(2,3)))
