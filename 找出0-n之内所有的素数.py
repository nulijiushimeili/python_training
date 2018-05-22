import math


# 找出0-n以内的素数
def prime(n):
    number = []
    prime_number = []
    for i in range(0, n, 1):
        number.append(True)
    number[0] = False
    number[1] = False
    for i in range(2, int(math.sqrt(n)), 1):
        for j in range(i * i, n, i):
            number[j] = False
    for i in range(0, n, 1):
        if number[i]:
            prime_number.append(i)
    return prime_number


ans = prime(10000)
print(len(ans))
print(ans)
