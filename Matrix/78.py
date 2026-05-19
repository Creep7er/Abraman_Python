import random
from math import inf

M = 5 #int(input("M? "))
N = 5 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(-10, 10))
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
for m in range(M):
    for i in range(M):
        for j in range(M - 1):
            if matrix[j][m] < matrix[j + 1][m]:
                matrix[j][m], matrix[j + 1][m] = matrix[j + 1][m], matrix[j][m]


for m in range(M):
    print(matrix[m])