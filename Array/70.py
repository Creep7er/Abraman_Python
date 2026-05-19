import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 10))
print(A)

# ------- Заполнение массива

for i in range(int(len(A)/2)):
    print(A[i+int(len(A)/2)])
    kekus = A[i]
    A[i] = A[i+int(len(A)/2)]
    A[i+int(len(A)/2)] = kekus

print(A)