import random
from math import inf

M = 5 #int(input("M? "))
N = 5 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(m*10 + n)
    matrix.append(row)

print("Матрица")
for m in range(M):
    print(matrix[m])

print("Ответ")

for i in range((M + 1) // 2):
    for j in range(M - 1 - i, i + 1):
        matrix[i][j] = 0

for i in range((M + 1) // 2, M):
    for j in range(M - i - 1, i + 1):
        matrix[i][j] = 0

for m in range(M):
    print(matrix[m])