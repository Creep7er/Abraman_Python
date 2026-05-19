import random
from math import inf

# ---- Создание массива
N = int(input())

A = []
B = []
for x in range(N):
    A.append(random.randint(1, 99))

for x in range(N):
    B.append(random.randint(1, 99))

print(A)
print(B)
# --- Создание массива
C = []
for i in range(len(A)):
    C.append(A[i])

for i in range(len(B)):
    A[i] = B[i]

for i in range(len(B)):
    B[i] = C[i]

print(A)
print(B)

