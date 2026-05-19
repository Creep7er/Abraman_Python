from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    kek = random.randint(0, 100)
    lol = random.randint(0,2)
    if lol == 1:  
        for n in range(1, N+1):
            row.append(kek + n)
    elif lol == 2:  
        for n in range(1, N+1):
            row.append(kek - n)
    else:
        for n in range(1, N+1):
            row.append(random.randint(0, 100))
    matrix.append(row)
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
flag_plus = False
flag_minus = False
counter = 0
answer = []
for m in range(M):
    for n in range(1, N):
        if matrix[m][n-1] < matrix[m][n]:
            flag_plus = True
        else:
            flag_plus = False
            break
    for n in range(1, N):
        if matrix[m][n-1] > matrix[m][n]:
            flag_minus = True
        else:
            flag_minus = False
            break
    if flag_plus or flag_minus:
        min_kek = inf
        for n in range(N):
            if matrix[m][n] <= min_kek:
                min_kek = matrix[m][n]
        answer.append(min_kek)
            

if not(len(answer)):
    print(0)
else:
    print(min(answer))