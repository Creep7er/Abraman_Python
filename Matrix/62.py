from math import inf
import random
K = 2 -1 #int(input("K? ")) - 1
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
    matrix[m].pop(K)
N -=1
for m in range(M):
    print(matrix[m])
