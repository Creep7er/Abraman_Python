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
"""for S in range(M+N-1, -1, -1):
    for q in range(1, S-1):
        matrix[S][S+q] = 0"""

for i in range(M-2):
    for j in range(i+1, M-i-1):
        matrix[i][j] = 0

for m in range(M):
    print(matrix[m])



