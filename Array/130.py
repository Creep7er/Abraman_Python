import random
import math
# ------- Заполнение массива
N = 11  # int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(3, 5))
A = [1, 1, 3, 3, 2, 4, 1, 4, 4, 5, 5]
N = len(A)
#A.sort()
print(A)
# ------- Заполнение массива

K = -math.inf
lena = 1
index2 = len2 = None
x = N-1

top = []
top_max = -math.inf
for x in range(1, N):
    if A[x] != A[x-1]:
        if lena > K:
            top = [x-lena]
            K = lena
        elif lena == K:
            top.append(x-lena)
        lena = 1
    elif x == N-1:
        lena += 1
        if lena == K:
            top.append(N-1)    

    else:
        lena += 1
print(K, top)

for i in top[::-1]:
    A.insert(i, A[i])
    print(f"Добавил {A[i] }в {i}")
print(A) 