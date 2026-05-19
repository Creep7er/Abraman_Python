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
for i in range(N):
    if A[i] % 2 == 0:
        B.append(A[i])

print(B, len(B))
