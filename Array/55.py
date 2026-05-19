import random
from math import inf

# ---- Создание массива
N = 16
while not (N <= 15):
    N = int(input("ВВЕДИТЕ N "))

A = []
B = []
for x in range(N):
    A.append(random.randint(1, 99))

print(A)
# --- Создание массива
for i in range(1, N-1, 2):
    B.append(A[i])

print(B, len(B))
