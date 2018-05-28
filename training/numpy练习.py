import numpy as np

# 创建一个4*4的数组
a1 = np.random.rand(4, 4)
print(a1)

# python 数组在不同的计算机上计算的结果可能不同
# 使用mat()函数将数组转换成矩阵
print(type(a1))
# <class 'numpy.ndarray'>
a2 = np.mat(a1)
print(a2)
print(type(a2))
# <class 'numpy.matrixlib.defmatrix.matrix'>

# 矩阵求逆
a3 = a2.I
print(a3)

# 得到的是单位矩阵,主对角线上的数都是1,其他位置都是0
a4 = a2 * a3
print(a4)
# 计算机计算的时候会有误差,所以有趋近于0的小数

# 创建单位矩阵
a5 = np.eye(4, 4)
print(a5)

# numpy的ndarray:一种多维数组对象
data1 = [1, 2, 4, 5, 6.23]
print(data1)

# 将列表转换成numpy的数组
arr1 = np.array(data1)
print(arr1)

# 二维数组
data2 = [[1, 2, 3, 4],
         [5, 6, 7, 8]]
print(data2)
arr2 = np.array(data2)
print(arr2)

# 返回数组的维度
print(arr2.ndim)

# 返回数组的形状
print(arr2.shape)

# 返回数组的数据类型
print(arr1.dtype)
print(arr2.dtype)

# 创建10个元素全为0 的数组
arr3 = np.zeros(10)
print(arr3)

# 元素为0的三行四列的数组
arr4 = np.zeros((3, 4))
print(arr4)

# 嵌套的数组
arr5 = np.empty((2, 3, 2))
print(arr5)

# python range的np.array版
arr6 = np.arange(15)
print(arr6)

# 创建一个矩阵
A = np.arange(12).reshape((3, 4))
print(A)

# 参照A的形状创建全为1 的矩阵
B = np.ones_like(A)
print(B)

# zeros,zeros_like 同ones的用法

# 创建4*4的单位方阵
C = np.eye(4)
print(C)
D = np.identity(4)
print(D)

# 指定数据类型
arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1.dtype)

# 显式的转换np的array的数据类型
arr2 = np.array([1, 2, 3, 4, 5, 6])
print(arr2.dtype)
float_arr2 = arr2.astype(np.float)
print(float_arr2.dtype)

# 将浮点类型的数据转换成整数类型
arr3 = np.array([2.2, 3.3, 4.55, 6.23, 1.22])
# 结果是直接将小数部分的数值抹掉
print(arr3.astype(np.int32))

# 也可以将数值类型的字符串转换为数值
num_strings = np.array(["23", "34", "22", "3.44"])
num = num_strings.astype(float)
# 如果转换过程中有的字符串不能转换成数值类型,会抛异常
print(num.dtype)
# 注意:调用astype无论如何都会创建出一个新的数组(原始数据的copy),
# 即使dtype是相同的,也还是一样会复制新的数组

# 浮点类型的数值只是近似值,在复杂的运算过程中会出现浮点错误,
# 一般比较浮点类型的值,使用减法,当误差值在一定范围内,则两个数相等

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
# 数组与标量之间的运算是将每个标量的值传递到各个元素
arr2 = arr1 * arr1
print(arr2)
print(arr1 ** 2)
# 不同数组之间的运算叫做广播,
arr3 = np.array([1, 2, 3])
print(arr1 * arr3)
# [[ 1  4  9]
#  [ 4 10 18]]

# 数组的索引与切片,返回指定区域的元素
arr1 = np.arange(10)
print([3, 4, 5])
print(arr1[2:5])
arr2 = arr1[5:8]
arr2[:] = 50
print(arr1)
# [ 0  1  2  3  4 50 50 50  8  9]
# 将原数组的值改变了
# numpy的操作直接就是对数组本身进行操作
# 如果想要复制一个副本的话
arr3 = arr1[5:7].copy()
print(arr3)

arr1 = np.arange(9).reshape(3, 3)
print(arr1)
# 对每个元素递归访问,获取指定位置的元素,这样的做法效率不高
print(arr1[2][2])
# 推荐使用这种方法
print(arr1[2, 2])

#
arr3 = np.array([[[1, 2, 3],
                  [4, 5, 6]],
                 [[7, 8, 9],
                  [10, 11, 12]]])
print(arr3[0])
# 给数组赋值标量
arr3[0] = 50
print(arr3)

arr = np.arange(15).reshape((3, 5))
# 矩阵的转置
print(arr.T)
# 矩阵乘法
print(np.dot(arr, arr.T))
print(arr.dot(arr.T))
print(arr)

# 布尔值索引
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.random.rand(7, 4)
print(names)
print(data)
print(names == "Bob")
# ==Bob 是第一行和第四行,接着选择相应的列
print(data[names == "Bob", 2:])
print(data[names == "Bob", 3])
# ==Will 的是第三行和第五行
print(data[names == "Will"])
# ...
mask = (names == "Bob") | (names == "Joe")
print(mask)
print(data[mask])
# 通过布尔型索引选取数组中的数据,将总是创建数据的副本
# 即使返回一模一样的数组也是如此
# 注意点: python关键字and | or 在布尔型数组中无效

# 将数组中小于0的数组赋值成0
data[data < 0] = 0
# 通过一维布尔数组设置整行或整列的值也很简单
data[names != "Bob"] = 6
# 可以将对应的行的值都设置成6

# 花式索引 Fancy indexing
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr)
# 以特定的顺序选取子集
print(arr[[4, 5, 2, 1]])
# 使用负数索引将从末尾开始选取
print(arr[[-2, -3, -4]])
