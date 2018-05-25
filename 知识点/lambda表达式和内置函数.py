# lambda表达式:快速定义单行的最小函数,inline的匿名函数


# lambda创建单行的匿名函数
g = lambda x: x * 2
print(g(5))

# map(function,iterable)
# 使用map遍历集合,并对集合中的元素进行操作
items = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, items)))
test_map = list(map(g, [4, 5, 6]))
print(test_map)

# filter(function,iterable)
test_filter = list(filter(lambda x: x > 2, [1, 3, 4]))
print(test_filter)

# --------内置函数----------------------------------
# 绝对值
print(abs(-5.5))

# bin()将整数数值转换成二进制数值
print(bin(10))

# ascii(ojb), repr()将一个对象转换成可以打印的字符串
print(ascii(["hello"]))

# bool(x)
print(bool())  # 参数为0或不给参数时,返回False
print(bool(-5))  # 其他数据返回True

# 将字符串转换为ASCII码
a = bytearray(b"hello")
print(list(a))

# chr()将数值转换为字符,ord()将字符转换为数值
print(chr(97))
print(ord("A"))

# oct() 将一个数值转换为8进制数值
print(oct(10))
# hex(x) 将一个数值转化为16进制的数值
print(hex(16))


# ------------------------------------------------
# callable()
def f():
    print("这个函数可以调用")


print(callable(f))
a = 10
# 数值类型不是函数,不能被调用
print(callable(a))  # False


# -----------------------------------------------

# compile():编译一个源,返回一个代码对象,该代码对象可以用来作为exec()或者eval()的参数

# ------------------------------------------------
# property(fget=None, fset=None, fdel=None, doc=None)
# property()将类的方法作为属性来访问
class C:
    def __init__(self):
        self.__x = None

    def getx(self):
        return self.__x

    def setx(self, value):
        self.__x = value

    def delx(self):
        del self.__x

    x = property(getx, setx, delx, "I'm the 'x' property.")


c = C()
c.x = "Jeck"  # 相当于调用setx()方法
print(c.x)  # 相当于调用getx()方法
del c.x  # 相当于调用delx()方法

# print(c.x)

# --------------------------------------------------
# pow(x, y[, z])：pow(x, y)相当于x**y，pow(x, y, z)相当于pow(x, y) % z。

# set() set的构造函数
# object()
# tuple() tuple的构造函数

# setattr(object, name, value): 为一个对象的name属性设置一个value值

# reversed() 翻转序列
print(list(reversed([1, 2, 3, 4, 5])))

# range(start, stop[, step])

# next()  迭代器的下一个

# sorted()
z = [5,4,3,2]
print(sorted(z))
print(list(reversed(sorted(z))))

# pow(x, y)  相当于x ** y

# zip() 将序列打包成一个个元祖
t = zip([1, 2, 3, 4, 5])
for i in t:
    print(i)

# iter()  返回一个可迭代的对象
it = iter(z)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 返回类中所有的属性
print(vars(C))

# reduce在python3中不是内置函数,放在functools这个包了
from functools import reduce
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
