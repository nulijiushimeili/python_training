import numpy as np
import pandas as pd

# 排序,根据条件对数据集进行排序
obj = pd.Series(range(4), index=list("dabc"))
print(obj)
print(obj.sort_index())

# 对于DataFrame可以对任意一个轴的索引进行排序
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=["three", "one"],
                     columns=list("dabc"))
print(frame)
# 按行排序
print(frame.sort_index())
# 按列排序
print(frame.sort_index(axis=1))
# 按列降序
print(frame.sort_index(axis=1, ascending=False))

# 对Series进行排序,
obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())

# 对于任何缺失值,排序完成后都会被放在末尾

# 对多个列的值进行排序
frame = pd.DataFrame({"b": [4, 7, -3, 2],
                      "a": [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by="b"))
# 对多个列的值进行排序,sort_index(by=)这个方法已经过时
print(frame.sort_values(by=["a", "b"]))

# 默认情况下，rank是通过“为各组分配一个平均排名”的方式破坏平级关系的
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())

# 也可以根据在原来数据中出现的顺序进行排名
print(obj.rank(method="first"))
# 降序排名
print(obj.rank(ascending=False, method="max"))

# DataFrame可以在行和列上进行计算排名
frame = pd.DataFrame({"b": [4.3, 7, -3, 2],
                      "a": [0, 1, 0, 1],
                      "c": [-2, 5, 8, -2.5]})
print(frame)
print(frame.rank())
print(frame.rank(axis=1))

# 排名时用于破坏平衡关系的method选项
# "average"  默认,为各个值分配平均排名
# "min"  使用整个分组的最小排名
# "max"  使用整个分组的最大排名
# "first"  使用原始数据在数据集中出现的顺序排名

# 带有重复的索引值
# 推荐索引唯一但不是必须的
# 如果一个索引对应多个值,则会返回一个Series,
# 如果一个索引对应一个值,则返回一个标量值
obj = pd.Series(range(5), index=list("AABBC"))
print(obj)
# 查看DF的索引是否是唯一的
print(obj.index.is_unique)
print(obj["A"])
print(obj["C"])

# 带有重复索引对DF来说也是如此
df = pd.DataFrame(np.random.randn(4, 3), index=list("AABB"))
print(df)
# 返回的是一个DF
print(df.ix["B"])

# 汇总和计算描述统计
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=list("ABCD"),
                  columns=["one", "two"])
print(df)
print(df.sum())
# 通过轴确定对行求和,还是对列求和
print(df.sum(axis=1))
# NA 值会自动排除,除非真个切片都是NA
# 通过skipna=False可以禁用此功能
print(df.mean(axis=1, skipna=False))

# 参数说明
# axis  约减的轴,DF行用0,列用1
# skipna  排除缺失值,默认为True
# level  如果轴是层次化索引的,则根据level分组约减

# 间接统计
# 达到最大值的索引
print(df.idxmax())
# 达到最小值的索引
print(df.idxmin())
# 累加
print(df.cumsum())
# 一次性产生多个统计值, 汇总统计
print(df.describe())

# 描述和汇总统计
# count  非NA值的总数
# describe  汇总统计
# min,max  最大最小值
# argmin,argmax  最大最小值的索引位置
# idxmin,idxmax  最大最小值的索引值
# quantitle  计算样本的分为数
# sum  所有值的总和
# mean  值的平均数
# median  中位数
# mad  根据平均值计算绝对离差
# var  样本的方差
# std  样本的标准差
# skew  样本的偏度(三阶矩)
# kurt  样本的峰度(四阶矩)
# cumsum  样本的累计和
# cummin,cummax  样本累计最大最小值
# cumprod  样本的累乘积
# diff  计算样本的一阶差分(对时间序列很有用)
# pct_change  尖酸样本的百分数变化

# # 相关系数和协方差
# import pandas.io.data as web
#
# all_data = {}
# for ticket in ["AAPL","IBM","MSFT","GOOG"]:
#     all_data[ticket] = web.get_data_yahoo(ticket, "1/1/2000","1/1/2010")
# price = pd.DataFrame({tic:data["Adj Close"]
#                       for tic,data in all_data.items()})
# volume = pd.DataFrame({tic:data["Volume"]
#                        for tic,data in all_data.items()})
# print(price)
# print(volume)
