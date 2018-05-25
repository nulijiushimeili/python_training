class Cat:
    name = "cat"

    def __init__(self, name, color="white"):
        self.name = name
        self.color = color

    # 定义类方法
    @classmethod
    def jump(cls):
        print("{} jump".format(cls.name))
        print("The cat jume to the wall")

    def run(self):
        print("{} is runing ...".format(self.name))


class Bosicat(Cat):

    def set_new_name(self, new_name):
        self.name = new_name

    def eat(self):
        print("{} is eating ...".format(self.name))


# 测试类
bs = Bosicat("波波")
print("bs的名字是{},毛色是{}".format(bs.name, bs.color))
bs.eat()
bs.run()
bs.set_new_name("阿狸")
print("bs的名字是{},毛色是{}".format(bs.name, bs.color))

# 测试类的属性
c = Cat("小狸猫")
c.jump()
Cat.jump()  # 类的方法可以不用实例化就直接调用
Cat.run(c)


# 静态方法
class People(object):
    __country = "China"

    # 声明一个静态方法
    @staticmethod
    def get_country():
        return People.__country


print(People.get_country())
