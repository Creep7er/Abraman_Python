from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(0, 5))
    matrix.append(row)

print("Матрица")
for m in range(M):
    print(matrix[m])

print("Ответ")
for m in range(M // 2):
    for n in range(N // 2):
        matrix[m + M // 2][n], matrix[m][n + N // 2] = matrix[m][n + N // 2], matrix[m+ M // 2][n]



for m in range(M):
    print(matrix[m])