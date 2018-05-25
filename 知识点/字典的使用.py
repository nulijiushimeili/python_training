# 登记学生的信息
stu_a = {
    "name": "Jeck",
    "age": 22,
    "gender": 1,
    "hometown": "Beijing"
}

stu_b = {
    "name": "Mark",
    "age": 21,
    "gender": 1,
    "hometown": "Shanghai"
}

stu_c = {
    "name": "Junani",
    "age": 20,
    "gender": 0,
    "hometown": "Tianjin"
}


def stu_info(stu):
    """自我介绍"""
    for key, value in stu.items():
        print("{}:{}".format(key, value))


stu_info(stu_a)
stu_info(stu_b)
stu_info(stu_c)

# 遍历字典中的key
for key in stu_a.keys():
    print(key)

# 遍历字典中的value
for value in stu_b.values():
    print(value)

# 修改字典中的元素
stu_a["name"] = "Macle"
print(stu_a["name"])

# 访问不存在的元素的时候会抛异常
# print(stu_a["email"])

# 创建一个字典,并使用内置函数删除
info = {'name': 'monitor', 'sex': 'f', 'address': 'China'}
print('删除前:%s' % info)
# del(info)

# 删除字典后,访问抛异常
# print('删除后,%s' % info)

# 清空字典中的元素
info.clear()
print(info)

# 查看字典中是否包含某个属性
print(info.get("name"))

# 字典中添加元素,可以不给定value
print(info.setdefault("name", "Gosi"))
print(info)

