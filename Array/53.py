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
for i in range(N):
    if A[i] > B[i]:
        C.append(A[i])
    else:
        C.append(B[i])

print(C)
