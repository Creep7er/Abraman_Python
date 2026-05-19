import random
import math
# ------- Заполнение массива
N = 20  # int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(3, 5))
#A = [1, 1, 3, 3, 2, 4, 1, 4, 4, 5]
A.sort()
print(A)
# ------- Заполнение массива

K = -math.inf
lena = 1
index2 = len2 = None
x = N-1
while x > 0:

    if A[x] != A[x-1]:
        if lena > K:
            K = lena
            index_x = x
            
        lena = 1
    else:
        lena += 1
    x -= 1
    #print(x)
A.insert(index_x, A[index_x])
print(f"Добавил в {index_x}")
print(A)