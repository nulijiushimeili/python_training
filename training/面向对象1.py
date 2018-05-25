

class SweetPotato:
    """这是一个烤地瓜的类"""

    # 第一初始化方法
    def __init__(self):
        self.cookedLevel = 0
        self.cookedStatus = "生的"
        self.condiments = []

    # toString()方法
    def __str__(self):
        msg = "地瓜"
        if len(self.condiments) > 0:
            msg = msg + "加了("

            for temp in self.condiments:
                msg = msg + temp + ", "
            msg = msg.strip(", ")

            msg += ")," + self.cookedStatus
        return msg

    # 烤地瓜的方法
    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedStatus = "烤成灰了"
        elif self.cookedLevel > 5:
            self.cookedStatus = "考好了"
        elif self.cookedLevel > 3:
            self.cookedStatus = "半生不熟"
        else:
            self.cookedStatus = "生的"

    # 添加配料
    def add_condiments(self, condiments):
        self.condiments.append(condiments)


# 测试类的功能
my_sweet_potato = SweetPotato()
print("烤地瓜... 烤地瓜喽...")
print(my_sweet_potato.cookedLevel)
print(my_sweet_potato.cookedStatus)
print(my_sweet_potato.condiments)
my_sweet_potato.cook(4)
print(my_sweet_potato.cookedStatus)
my_sweet_potato.add_condiments("番茄酱")
print(my_sweet_potato.condiments)
my_sweet_potato.cook(6)
my_sweet_potato.add_condiments("糖")
print(my_sweet_potato.condiments)
print(my_sweet_potato.cookedStatus)
print(my_sweet_potato)


# ------------------------------------------------
# __new__(cls)方法
# 1.__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
#
# 2.__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
#
# 3.__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

class A(object):

    # 在new方法后执行实例化对象
    def __init__(self):
        print("这是 init 方法")

    # 这个方法会在init方法之前先对class进行操作
    def __new__(cls):
        print("这是 new 方法")
        return object.__new__(cls)


A()
