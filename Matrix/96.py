import random
from math import inf

M = 5 #int(input("M? "))
N = 5 #int(input("N? "))
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

for y in range(M-2, -1, -1):
    for x in range(M-y-1):
        matrix[x][y+x+1], matrix[y+x+1][x] = matrix[y+x+1][x], matrix[x][y+x+1]


print("Матрица")
for m in range(M):
    print(matrix[m])
