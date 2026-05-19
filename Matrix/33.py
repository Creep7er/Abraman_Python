from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
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
posit = 0
negat = 0
iterator = 0
flag = False
for n in range(N):
    for m in range(M):
        if matrix[m][n] > 0:
            posit += 1
        elif matrix[m][n] < 0:
            negat += 1
    if negat == posit:
        flag = n
    else:
        negat = 0
        posit = 0

if flag:
    print("ответ", flag + 1)
    for m in range(M):
        print(matrix[m][flag])
else:
    print("Mission failed")
    
