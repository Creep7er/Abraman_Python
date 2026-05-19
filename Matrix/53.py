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
maximus = -inf
maximus_cord = 0
minimus = inf
minimus_cord = 0
cord = 0
for n in range(N):
    for m in range(M):
        if matrix[m][n] > 0:
            flag = True
        else: flag = False; break
    if flag:
        cord = n
if cord:
    print("заменил")
    for m in range(M):
        matrix[m][0], matrix[m][cord] = matrix[m][cord], matrix[m][0]
for m in range(M):
    print(matrix[m])    