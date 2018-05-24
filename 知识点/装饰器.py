# 一个最简单的装饰器
# def func1():
#     print("Tom is a good man")
#
#
# def outer(func):
#     def inner():
#         print("*" * 20)
#         func()
#     return inner
#
#
# f = outer(func1)
# f()

# # 一个稍微复杂点的装饰器
# def outer(func):
#     def inner(age):
#         if age < 0:
#             age = 0
#         func(age)
#
#     return inner
#
#
# # 使用注解的时候,要将装饰器方法放在原函数前面,否则会找不到
# @outer
# def say(age):
#     print('Tom is %d years old' % age)
#
#
# # 这句话可以不用写了,使用@outer代替
# # f = outer(say)
# say(-2)


# 制作一个通用的装饰器
def outer(func):
    def inner(*args, **kwargs):
        print("Hello,", end="")
        func(*args, **kwargs)
    return inner


@outer
def say(name="Tom", age=15):
    print("I am {}, I am {} years old.".format(name, age))


say(name="Join", age=12)
say(name="Jeck")

