from math import inf
import random
K = 2 #int(input("K? ")) - 1
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
maximus = -inf
maximus_cord = 0 
for m in range(M):
    for n in range(N):
        if matrix[m][n] > maximus:
            maximus = matrix[m][n]
            maximus_cord = m
row_k = matrix[maximus_cord]
matrix.insert(maximus_cord, row_k)
M+=1
for m in range(M):
    print(matrix[m])
