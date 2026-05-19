from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    row.append(100 - m)
    for n in range(1, N+1):
        row.append(random.randint(0, 100))
    row.append(120 - m)
    matrix.append(row)
N += 2
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
flag = False
counter = 0
for n in range(N):
    for m in range(1, M):
        if matrix[m-1][n] > matrix[m][n]:
            flag = True
        else:
            flag = False
            break
    if flag:
        counter += 1

print(counter)