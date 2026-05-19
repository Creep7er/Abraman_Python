import random
from math import inf

M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(0, 10))
    matrix.append(row)

print("Матрица")
for m in range(M):
    print(matrix[m])

print("Ответ")

for i in range(M):
    for j in range(N):
        i2 = M - 1 - i
        j2 = N - 1 - j

        if i > i2 or (i == i2 and j >= j2):
            continue

        matrix[i][j], matrix[i2][j2] = matrix[i2][j2], matrix[i][j]

for m in range(M):
    print(matrix[m])