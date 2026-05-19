from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    row.append(100 + m)
    for n in range(1, N+1):
        row.append(random.randint(0, 100))
    row.append(120 - m)
    matrix.append(row)
N += 2
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
flag_plus = False
flag_minus = False
counter = 0
answer = []
for n in range(N):
    for m in range(1, M):
        if matrix[m-1][n] < matrix[m][n]:
            flag_plus = True
        else:
            flag_plus = False
            break
    for m in range(1, M):
        if matrix[m-1][n] > matrix[m][n]:
            flag_minus = True
        else:
            flag_minus = False
            break
    if flag_plus or flag_minus:
        min_kek = inf
        for m in range(M):
            if matrix[m][n] <= min_kek:
                min_kek = matrix[m][n]
        answer.append(min_kek)
            
if not(len(answer)):
    print(0)
else:
    print(min(answer))