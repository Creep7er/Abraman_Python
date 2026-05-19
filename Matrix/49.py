from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(0, 100))
    matrix.append(row)

print("Матрица")
for m in range(M):
    print(matrix[m])

print("Ответ")


for m in range(M):
    maximus = -inf
    maximus_cord = 0
    minimus = inf
    minimus_cord = 0
    for n in range(N):
        if matrix[m][n] > maximus:
            maximus = matrix[m][n]
            maximus_cord = n
        if matrix[m][n] < minimus:
            minimus = matrix[m][n]
            minimus_cord = n
            
    matrix[m][maximus_cord], matrix[m][minimus_cord] = matrix[m][minimus_cord], matrix[m][maximus_cord]
for m in range(M):
    print(matrix[m])


    