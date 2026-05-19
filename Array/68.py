import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 10))
print(A)

# ------- Заполнение массива

maxs = -inf
mins = inf
max_index = -1
min_index = -1

for i in range(len(A)):
    if A[i] >= maxs:
        maxs = A[i]
        max_index = i

    if A[i] <= mins:
        mins = A[i]
        min_index = i

print(mins, maxs)

A[max_index], A[min_index] = A[min_index], A[max_index]

print(A)