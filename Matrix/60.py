from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(-100, 100))
    matrix.append(row)

print("Матрица")
for m in range(M):
    print(matrix[m])

print("Ответ")
for m in range(M):
    for n in range(N // 2):
        matrix[m][N-1-n], matrix[m][n] = matrix[m][n], matrix[m][N-1-n]

for m in range(M):
    print(matrix[m])
