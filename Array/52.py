import random
from math import inf

# ---- Создание массива
N = int(input())

A = []
B = []
for x in range(N):
    A.append(random.randint(1, 99))

print(A)
# --- Создание массива

for i in range(len(A)):
    if A[i] < 5:
        B.append(2*A[i])
    else:
        B.append(A[i] / 2)

print(B)


