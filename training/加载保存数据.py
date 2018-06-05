# 数据加载,存储与文件格式
import pandas as pd


# read_csv  从文件,URL,文件型对象中加载带分隔符的数据,默认分割符是逗号
# read_table  从文件,URL,文件型对象中加载带分隔符的数据,默认分割符是制表符("\t)
# read_fwf  读取定宽列格式数据
# read_clipboard  读取剪贴板的数据

df = pd.read_csv(r"D:\mycode1\program\python_training\training\decision_tree_data.csv")
print(df)

# read_csv & read_table函数的参数
# path  文件的路径
# sep | delimiter  用于对行中各个字段进行拆分的字符序列或正则表达式
# header  作为列名的行号
# index_col  用作航索引的列编号或列名
# names  用于结果的列名列表
# skiprows  需要忽略的行数,从0开始
# na_values  一组用于替换na的值
# comment  用于将注释信息从行尾拆分出去的字符
# parse_datas  尝试将数据解析为日期
# keep_date_col
# converters
# dayfirst
# date_parser  用于解析日期的函数
# nrows  需要读取的函数
# iterator
# chunksize  文件块的大小
# skip_footer  需要忽略的行数,从文件末尾开始算起
# verbose  打印各种解析器输出信息
# encoding  用于Unicode的文本编码格式
# squeeze  如果数据经解析,仅含一列,则返回Series
# thousands

# 将数据写出到文本格式
# df.to_csv("D:/tmp/data.csv")

# 用于保存的参数
# sep="\t"  只用制表符作为分割符
# na_rep="NULL"  将NA值替换成空格



















































