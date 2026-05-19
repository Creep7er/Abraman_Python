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
row_1 = [1, 1, 1, 1, 1, 1]
matrix.append(row_1)
M += 1
row_1 = [1, 1, 1, 1, 1, 1]
matrix.append(row_1)
M += 1
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
arra = []
counter = 0
for m in range(M):
    arra = []
    flag = False
    for n in range(N):
        for n_1 in range(n, N):
            if matrix[m][n] != matrix[m][n_1]:
                counter += 1
                flag = True
                break
        if flag:
            break
print(counter)
        