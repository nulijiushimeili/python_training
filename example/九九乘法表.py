# 九九乘法表


# for循环实现
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}".format(j, i, i * j), end="\t")
    print()

# while循环实现
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("{}*{}={}".format(j, i, i * j), end="\t")
        j += 1
    i += 1
    print()


# 递归,不适合写99
def recurring(a=0, b=10):
    if a == b:
        return a
    if a < b:
        print(a)
        return recurring(a + 1)
    if b > a:
        print(b)
        return recurring(b + 1)


print(recurring(1))


