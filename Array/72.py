import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 10))
print(A)

# ------- Заполнение массива

K = int(input('K '))
L = int(input('L '))

for i in range(K, int(L/2)+1):
    print(A[abs(len(A)-1-i)], A[i])
    kekus = A[i]
    A[i] = A[abs(len(A)-1-i)]
    A[abs(len(A)-1-i)] = kekus

print(A)
