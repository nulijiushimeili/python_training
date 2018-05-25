class Singleton(object):
    __instance = None

    def __new__(cls, name, age):
        # 如果__instance属性为None
        # 就创建这个对象,
        # 否则直接返回这个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


# 两次实例化返回的是同一个对象
a = Singleton(name="xiaoming", age=15)
b = Singleton(name="xiaohong", age=20)

print(id(a))
print(id(b))
# 79066640
# 79066640
a.name = "Jack"
b.name = "Tom"
print(a.name, b.name)

