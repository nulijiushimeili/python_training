# # 写文件
# f = open("test.txt", "w")
# f.write("Hello word, I am here.")
# f.close()


# # 读文件
# f = open("test.txt", "r")
# print(f.read())
# f.close()

# 文件访问模式的参数说明
# a 追加内容
# rb 以二进制的方式只读
# wb 以二进制的方式写
# ab 以二进制的方式追加
# r+,w+ 打开文件用于读写
# rb+,wb+,ab+,a+,读写文件和追加,文件若不存在就创建


# # ------------复制文件-----------------------
# # 提示输入文件名
# oldFileName = input("请输入要copy的文件的名字")
#
# # 以读的方式打开
# oldFile = open(oldFileName, "rb")
#
# # 提取文件的后缀
# fileFlagNum = oldFileName.rfind(".")
# if fileFlagNum > 0:
#     fileFlag = oldFileName[fileFlagNum:]
#
# print(fileFlagNum)
# print(fileFlag)
#
# # 组织新的文件的名字
# newFileName = oldFileName[:fileFlagNum] + "(附件)" + fileFlag
#
# # 创建新的文件
# newFile = open(newFileName, "wb")
#
# # 把旧文件中的数据,一行一行的复制到新的文件中
# for lineContent in oldFile.readlines():
#     newFile.write(lineContent)
#
# # 关闭文件
# newFile.close()
# oldFile.close()
#
# # ----------------复制文件完成---------------------------

# # ---------文件的定位读写----------------------
# f = open("test.txt", "r")
# string = f.read(3)
# print("读取的数据是:{}".format(string))
#
# # 查看当前指针的位置
# position = f.tell()
# print("当前的文件的位置:{}".format(position))
#
# # 重新设置指针的位置
# # seek(offset, whence)
# # offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
# # whence：可选，默认值为 0。
# # 给offset参数一个定义，表示要从哪个位置开始偏移；
# # 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
# f.seek(5, 0)
#
# # 查看当前指针的位置
# position = f.tell()
# print("当前的文件的位置:{}".format(position))
#
# # 重新从指定位置读取文件中内容
# string = f.read(3)
# print("读取的数据是:{}".format(string))
#
# # 重新设置位置
# f.seek(2, 0)
# string = f.read()
# print("读取的数据是:{}".format(string))
#
# # 关闭文件
# f.close()
#
# # -----------------------------------------------

import os

# # 删除文件
# os.remove("test.txt")

# # 创建文件夹
# os.mkdir("tmp")
#
# # 获取当前的目录
# os.getcwd()
#
# # 改变当前的目录
# os.chdir()
#
# # 删除文件夹
# os.rmdir("tmp")

# -------玩具程序:解析执行代码-----------------------
import time
f = open("testeval.py", "w+")
f.write("print(\"Hello word!\")")

time.sleep(1)

f = open("testeval.py", "r")
code = f.read()
# print(code)
eval(code)
f.close()
