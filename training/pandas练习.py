import pandas as pd
import numpy as np

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9]
        }
frame = pd.DataFrame(data)
print(frame)

new_frame = pd.DataFrame(data, columns=["year", "state", "pop"])
print(new_frame)

frame2 = pd.DataFrame(data,
                      columns=["year", "state", "pop", "debt"],
                      index=["one", "two", "three", "four", "five"])
print(frame2)
# 打印出列名
print(frame2.columns)
# 查看某一列的值
print(frame2["state"])
# 查看某一行的值
print(frame2.ix["three"])
# 对df的某一列进行赋值
frame2["debt"] = 16.5
print(frame2)
frame2["debt"] = np.arange(5.)
print(frame2)
# 给df的某一列赋值一个Series时,会对应相对应的行赋值,
# 没有赋值的,系统会给NA值
val = pd.Series([-1.2, -1.5, -1.7],
                index=["two", "four", "five"])
frame2["debt"] = val
print(frame2)
frame2["eastern"] = frame2.state == "Ohio"
print(frame2)
# 删除某一列的值
del frame2["eastern"]
print(frame2)

# 使用一个嵌套的字典创建dataframe
pop = {
    "Nevada": {2001: 2.4, 2002: 2.9},
    "Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6}
}
frame3 = pd.DataFrame(pop)
print(frame3)
print(frame3.T)

pdata = {
    "Ohio": frame3["Ohio"][:-1],
    "Nevada": frame3["Nevada"][:2]
}
# DataFrame可以接受各种类型的数据
df1 = pd.DataFrame(pdata)
print(df1)

# 给DF的行和列起名字
frame3.index.name = "year"
frame3.columns.name = "state"
print(frame3)
# DF的各个列的数据类型不同,值数组的数据类型会自动选择兼容所有列的数据类型
print(frame3.values)
print(frame2.values)

# index 是不可修改的数组
# index不可修改可以保证数据在多个数据结构之间安全共享
obj = pd.Series(range(3), index=["a", "b", "c"])
index = obj.index
print(index)
print(index[1:])
index = pd.Index(np.arange(3))
obj2 = pd.Series([1.5, -2.5, 0], index=index)
print(obj2.index is index)

# Index也类似于一个固定大小的集合
print(frame3)
print("Ohio" in frame3.columns)
print(2003 in frame3.index)

# 每个索引都有自己的一些属性和方法
# append()  连接一个的Index对象, 产生一个新的Index
# diff()  计算差集,并得到一个index
# intersection()  计算交集
# union()  计算并集
# isin()  返回是否包含于一个集合的布尔型数组
# delete()  删除索引i处的元素,并得到一个新的索引
# drop()  删除传入的值,并的到新的index
# insert()  将元素插入到指定的索引处
# is_monotonic()  当各个元素均大于前一个元素时,返回True
# is_unique()  当Index没有重复值时,返回True
# unique()  计算index中唯一值的数组

# 使用reindex()方法对数据进行重新索引
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
print(obj)
# 索引不当时,没有的索引会给它的值赋值NAN
obj2 = obj.reindex(["a", "b", "c", "d", "e"])
print(obj2)
# fill_value=0 给缺失值赋值0
obj = obj.reindex(["a", "b", "c", "d", "e"], fill_value=0)
print(obj)

# 对于有序的数据,重新索引可能需要做一些插值处理,
# method选项即可达到次目的, 使用method=ffill可以实现值向前填充
obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
print(obj3.reindex(range(6), method="ffill"))
# reindex() 参数说明
# ffill 或 pad  向前填充值
# bfill 或 backfill  向后填充值

# 对于DF,reindex() 可以修改行或列,也可以同时修改
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=["a", "c", "d"],
                     columns=["Ohio", "Texas", "Cali"])
print(frame)

# 修改行的索引
frame2 = frame.reindex(["a", "b", "c", "d"])
print(frame2)

# 修改列的索引
states = ["Texas", "Utah", "Cali"]
frame3 = frame.reindex(columns=states)
print(frame3)

# 同时修改行和列的索引
frame4 = frame.reindex(index=["a", "b", "c", "d"],
                       columns=states)
print(frame4)
#
# 使用.ix[[],]重新索引, 有警告说不推荐使用
# frame5 = frame.loc[["a","b","c","d"], states]
# print(frame5)

# 丢弃指定轴上的项, 可以删除任意轴上的索引
obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
print(obj)
new_obj = obj.drop("c")
print(new_obj)
new_obj2 = obj.drop(["a", "c"])
print(new_obj2)
# 这个也可以
del obj["a"]
print(obj)

# 可以删除任意轴上的索引
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "color", "Utah", "newY"],
                    columns=["one", "two", "three", "four"])
print(data)
# 删除行
nd1 = data.drop(["color", "Ohio"])
print(nd1)
# 删除列
nd2 = data.drop("two", axis=1)
print(nd2)
nd3 = data.drop(["two", "four"], axis=1)
print(nd3)

# 数据的选取和过滤
obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
print(obj)
# 筛选第二行
print(obj["b"])
print(obj[1])
# 筛选第三行,第四行
print(obj[2:4])
# 筛选对应索引的值
print(obj[["b", "a", "d"]])
print(obj[[1, 3]])
# 条件筛选
print(obj[obj < 2])
# 按索引筛选
print(obj["b":"c"])
# 对指定索引的值进行修改
obj["a":"c"] = 5
print(obj)
