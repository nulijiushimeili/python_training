# lambda表达式:快速定义单行的最小函数,inline的匿名函数


# lambda创建单行的匿名函数
g = lambda x: x * 2
print(g(5))

# 使用map遍历集合,并对集合中的元素进行操作
items = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, items)))
test_map = list(map(g, [4, 5, 6]))
print(test_map)

# filter
test_filter = list(filter(lambda x: x > 2, [1, 3, 4]))
print(test_filter)
