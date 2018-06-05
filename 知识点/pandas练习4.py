import numpy as np
import pandas as pd

# 唯一值,值计数,成员资格(在不在数组里面)
obj = pd.Series(["c", "a", "d", "a", "a", "b", "b", "c", "c"])
# 返回Series的唯一值, 并进行约减统计
uniques = obj.unique()
print(uniques)
# 将唯一值结果排序
uniques.sort()
print(uniques)
# value_counts() 用于计算各个值在Series中出现的次数
print(obj.value_counts())
# isin() 计算Series各个值是否包含于传进来的值序列中,结果为布尔型数组
mask = obj.isin(["b", "c"])
print(mask)
print(obj[mask])

#
data = pd.DataFrame({"Q1": [1, 3, 4, 3, 4],
                     "Q2": [2, 3, 1, 2, 3],
                     "Q3": [1, 5, 2, 4, 4]})
print(data)
result = data.apply(pd.value_counts)  # .fillna(0)
print(result)
# 其实就是个词频统计，只是按列统计次数，比如第一列，有1个1，2个3，2个4，对应索引1填1，索引2填2，索引4填2

# 处理缺失数据
string_data = pd.Series(["arrdvark", "artichoke", np.nan, "vaocado"])
print(string_data)
# 查看数组中是否包含
print(string_data.isnull())
string_data[0] = None
print(string_data.isnull())

# NA处理方法
# dropna  根据各标签的值中是否存在确实数据对轴标签进行过滤,可以通过阈值调节对缺失值的容忍程度
# fillna  用指定值或插值方法(ffill | bfill)填充确实数据
# isnull  返回一个含有布尔值的对象,这些布尔值表示哪些是缺失值NA该对象的类型与源类型一样
# notnull  isnull的否定式

# 过滤缺失数据
data = pd.Series([1, np.nan, 3.5, np.nan, 7])
useful_data = data.dropna()
print(data)
useful_data1 = data.notnull()
print(useful_data1)

# 对于DataFrame,dropna()是丢失含有缺失数据的行
data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],
                     [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
cleaned = data.dropna()
print(data)
print(cleaned)
# 如果只是想丢弃全部是NA的行或列时,设置参数how=all
useful_data2 = data.dropna(how="all")
print(useful_data2)
# 如果是要丢弃列,需要传入参数axis=1
data[4] = np.nan
print(data)
useful_data4 = data.dropna(how="all", axis=1)
print(useful_data4)

#
df = pd.DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = np.nan
df.ix[:2, 2] = np.nan
print(df)
print(df.dropna(thresh=3))

# 填充确实数据,fillna(0),将na的数据替换成0
print(df.fillna(0))

# 如果是通过一个字典fillna,可以实现对不同的列赋值不同的值
# 第二列0.5,第三列0.8,序号是从0开始的
print(df.fillna({1: 0.5, 2: 0.8}))

# fillna会产生一个新的对象,也可以对现有的对象进行修改
_ = df.fillna(0, inplace=True)
print(df)

# 对reindex有效的插值方法也可以用于fillna
df = pd.DataFrame(np.random.randn(6, 3))
df.ix[2:, 1] = np.nan
df.ix[4:, 2] = np.nan
print(df)
print(df.fillna(method="ffill"))
#           0         1         2
# 0 -0.950161  1.312536 -1.698200
# 1  1.190343  0.043996 -0.162801
# 2 -0.915689  0.043996  0.089001
# 3 -0.334812  0.043996  1.032089
# 4  0.209182  0.043996  1.032089
# 5  0.714094  0.043996  1.032089

# limit=2 , 表示只替换2行的na值
print(df.fillna(method="ffill", limit=2))

# 将na值替换成平均值或者中位数,这将会很实用
data = pd.Series([1., np.nan, 3.5, np.nan, 7])
print(data.fillna(data.median()))

# fillna()的参数
# value  用于填充缺失值的标量值或字典对象
# method  插值方式,如果函数调用时,没有指定其他参数的话,默认为ffill
# axis  待填充数据的轴,默认axis=0
# inplace  直接修改数据本身,而不是产生新的数据集
# limit  向前和向后填充,可以连续填充的最大数量

# 层次化索引
data = pd.Series(np.random.randn(10),
                 index=[["a", "a", "a", "b", "b", "b", "c", "c", "d", "d"],
                        [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
print(data.index)
print(data["b"])
print(data["b":"c"])
print(data.ix[["b", "d"]])
print(data[:, 2])
# 层次化索引在数据重塑和基于分组的操作中扮演着重要的角色
print(data.unstack())
#           1         2         3
# a -0.304216  1.773147  0.288231
# b  0.900785 -0.132956  0.235423
# c  0.083242 -0.116443       NaN
# d       NaN  1.658410 -0.102021

# stack()是unstack()的逆运算
print(data.unstack().stack())

# 对于DataFrame,每条轴都可以有分层索引
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[["a", "a", "b", "b"],
                            [1, 2, 1, 2]],
                     columns=[["Ohio", "Ohio", "Colorado"],
                              ["Green", "Red", "Green"]])
print(frame)

# 每层索引都可以有名字
frame.index.names = ["key1", "key2"]
frame.columns.names = ["state", "color"]
print(frame)
# 通过分部的列索引,可以轻松的选取列分组
print(frame["Ohio"])

# 重排分级的顺序,交换双重索引的位置
df1 = frame.swaplevel("key1", "key2")
print(df1)

# 根据级别汇总统计
print(frame)
# 对行索引进行求和
print(frame.sum(level="key2"))
# 对指定的列组进行求和
print(frame.sum(level="color", axis=1))

# 使用DataFrame的列作为DataFrame的索引
frame = pd.DataFrame({"a": range(7), "b": range(7, 0, -1),
                      "c": ["one", "one", "one", "two", "two", "two", "two"],
                      "d": [0, 1, 2, 0, 1, 2, 3]})
print(frame)
frame2 = frame.set_index(["c", "d"])
print(frame2)
# 默认情况下,作为索引的列会被移除,如果要保留,则
frame3 = frame.set_index(["c", "d"], drop=False)
print(frame3)
# reset_index()和set_index()刚好相反,层次化索引的级别会被转移到列里面
print(frame2.reset_index())

# 关于pandas
ser = pd.Series(np.arange(3.))
print(ser)
# 如果是数值索引,不可以使用负数作为索引,会抛异常
# print(ser[-1]) XXXXX
ser2 = pd.Series(np.arange(3.), index=list("abc"))
print(ser2)
# 如果是非整数的索引,可以使用负数,这是没有歧义的
print(ser2[-1])
# 截取前两个数据
print(ser.ix[:1])

# ...
