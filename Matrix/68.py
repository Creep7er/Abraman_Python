from math import inf
import random
K = 2 -1 #int(input("K? ")) - 1
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

print("Ответ")
row = []
for n in range(N):
    row.append(0)
matrix.insert(K, row)

for m in range(M):
    print(matrix[m])
