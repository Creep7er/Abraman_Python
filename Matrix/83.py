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

matrix2 = []
for m in range(M):
    row = []
    for n in range(N):
        row.append(matrix[m][n])
    matrix2.append(row)

print("Ответ")

S = 0
for x in range(M-1):
    for y in range(M-1, M-2-x, -1):
        S += matrix[y][2*m-x-y]
        print("@", matrix[y][2*m-x-y])
    print(S)
    S = 0
    for y in range(x, -1, -1):
        S += matrix[y][x-y]
        print("@", matrix[y][x-y])
    print(S)
    S = 0

