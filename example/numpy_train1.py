import numpy as np

A = np.array([[1, 2],
              [3, 4]])

print(A)

# 矩阵的维数
print(A.ndim)
# 矩阵的形状
print(A.shape)
# 矩阵的元素的个数
print(A.size)

# 生成一个矩阵
B = np.array([1, 2, 3, 4], dtype=np.int32)
print(B.dtype)

# 生成一个范围内等距的数组
linspace_a = np.linspace(0, 100, 5)
print(linspace_a)

C = np.arange(0, 12).reshape(3, 4)
print(C)
# 矩阵元素的累加
print(C.cumsum())

# 矩阵的点乘
D = np.arange(13, 25).reshape(4, 3)
print(D)
F = C.dot(D)
print(F)
G = np.dot(C, D)
print(G)

# 查看矩阵中对应的元素
print(G[2, 2])
print(G[2][2])

# 查看矩阵某一行和某一个列的值
print(G[1:2])
print(G[:1])
for row in G:
    print(row)

for col in G.T:
    print(col)
H = np.array([2, 2, 2])[:, np.newaxis]
I = np.array([1, 1, 1])[:, np.newaxis]
print(H)
print(I)
# 纵向合并矩阵
J = np.vstack((H, I))
print(J)
# 横向合并矩阵
K = np.hstack((H, I))
print(K)

L = np.arange(1, 17).reshape(4, 4)
print(L)
# 小于设定的最小值,则赋值最小值
# 大于设定的最大值,则赋值最大值
M = np.clip(L, 5, 10)
print(M)

# 横向两等分切分矩阵
N = np.split(L, 2, axis=0)
# 纵向两等分切分矩阵
O = np.split(L, 2, axis=1)
for row in N:
    print(row)
for row in O:
    print(row)

# 复制一个矩阵
P = L.copy()
print(P is L)

# 这个只是引用传递
Q = L
print(Q is L)
