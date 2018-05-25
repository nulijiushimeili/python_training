# __all__ = ["f1"]
# 使用__all__声明的函数可以通过import * 导入


def f1():
    print("f1函数被调用了")


def f2():
    print("f2函数被调用了")


# --------------------------------------------
# 列表推导式
a = [i for i in range(5)]
b = [i for i in range(10) if i % 2 == 0]
c = [(x, y) for x in range(3) for y in range(5)]
print(a)
print(b)
print(c)

# tuple, list, set之间可以相互转化
x = (1, 2, 3, 4, 5)
y = set(x)
z = list(y)
print(type(x))
print(type(y))
print(type(z))

# 使用set可以快速对list中的元素进行去重
l = [2, 3, 4, 5, 5, 6, 2, 6, 7]
print(list(set(l)))
