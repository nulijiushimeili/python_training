import numpy as np
import pandas as pd

# 数据的算术运算&自动数据对其
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=["a", "c", "e", "f", "g"])
print(s1)
print(s2)
# pandas可以对不同索引值的数据进行运算,在将对象相加时,
# 如果存在不同的索引对,则结果的索引就是该索引对的并集
# 自动数据对其会将不存在的值赋值NA,缺失值会在算术运算中传播
print(s1 + s2)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)),
                   columns=list("bcd"),
                   index=["Ohio", "Texas", "Color"])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                   columns=list("bce"),
                   index=["Utah", "Ohio", "Texas", "Oregon"])
print(df1)
print(df2)
print(df1 + df2)
# 结果为一个新的DataFrame
# 索引是两个旧的DataFrame的索引的并集

# 算术方法中填充值\
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list("ABCD"))
df2 = pd.DataFrame(np.arange(20.).reshape(4, 5),
                   columns=list("ABCDE"))
print(df1)
print(df2)
# 没有重叠的值会被NA填充
print(df1 + df2)
# 使用df1的add方法,传入一个df2以及一个fill_value参数:
# fill_value 表示如果值不存在的时候,自动使用这个参数指定的值进行填充
df3 = df1.add(df2, fill_value=0)
print(df3)
# 对Series和DataFrame重新进行索引时,也可以指定一个填充值
df4 = df1.reindex(columns=df2.columns, fill_value=0)
print(df4)

# 算术运算符说明
# add  用于加法(+)的方法
# sub  用于减法(-)的方法
# div  用于除法(/)的方法
# mul  用于乘法(*)的方法

# DataFrame与Series之间的运算
# 先做一个矩阵与一维数组运算的例子
arr = np.arange(12.).reshape((3, 4))
print(arr)
print(arr[0])
print(arr - arr[0])
# 矩阵的每一行都会减去数组的值
# 这就叫做广播
# DataFrame和Series之间的运算和上面这个例子一毛一样
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"])
series = frame.ix[0]
print(frame)
print(series)
print(frame - series)
# 默认情况下,DataFrame和Series之间的算术运算会将Series的索引匹配到DataFrame的列,然后沿着行一直向下广播

# 如果某个索引值在DataFrame的列或Series的索引中找不到,
# 则参与运算的两个对象会被重新索引形成并集然后广播运算
series2 = pd.Series(range(3), index=["b", "e", "f"])
print(frame + series2)

# 如果想要在列上进行广播,则必须使用算术运算方法
series3 = frame["d"]
print(frame)
print(series3)
print(frame.sub(series3, axis=0))
# 传入的轴号是希望匹配的轴,匹配DataFrame的行索引进行广播

# 函数的应用于映射
# numpy的ufuncs(元素级数组方法)也可以用来操作pandas对象
frame = pd.DataFrame(np.random.randn(4, 3),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"])
print(frame)
print(np.abs(frame))

# 另一个常见的操作是,将函数应用到各行各列所形成的一维数组上.
# DataFrame的apply方法即可实现此功能
f = lambda x: x.max() - x.min()
df1 = frame.apply(f)
print(df1)
df2 = frame.apply(f, axis=1)
print(df2)


# 常见的数组统计功能都被实现成DataFrame的方法,比如sum(),mean()
# 索引基本用不到apply方法

# 除了标量值外, 传递给apply的函数还可以返回由多个值组成的Series
def f(x):
    return pd.Series([x.min(), x.max()], index=["min", "max"])


df3 = frame.apply(f)
print(df3)

# 元素级的python函数也是可以使用的
# 格式化frame中的字符串
format2f = lambda x: "%.2f" % x
# 这里使用的是applymap
df4 = frame.applymap(format2f)
print(df4)

# 之所以使用applymap,是因为Series有一个应用于元素级函数的map方法
df5 = frame["e"].map(format2f)
print(df5)
