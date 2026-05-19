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
for S in range(M+N, -1, -1):

    for q in range(M-S):
        matrix[S][S+q] = 0
    
for m in range(M):
    print(matrix[m])



