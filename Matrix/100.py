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

matrix2 = []
for m in range(M):
    row = []
    for n in range(N):
        row.append(matrix[m][n])
    matrix2.append(row)

print("Ответ")
for i in range(M // 2):
    for j in range(i, M - 1 - i):
        matrix[i][j], matrix[j][M - 1 - i], matrix[M - 1 - i][M - 1 - j], matrix[M - 1 - j][i] = matrix[M - 1 - j][i], matrix[i][j], matrix[j][M - 1 - i], matrix[M - 1 - i][M - 1 - j]
for m in range(M):
    print(matrix[m])