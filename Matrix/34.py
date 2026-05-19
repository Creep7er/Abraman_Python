from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(2, 4))
    matrix.append(row)
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
chetnie = 0
chet_m = 0
flag = False
for m in range(M):
    for n in range(N):
        if matrix[m][n] % 2 == 0:
            chetnie = m
        else:
            chetnie = 0
            break
    if chetnie:
        chet_m = m

if chet_m:
    print(chet_m+1)
    print(matrix[chet_m])
else:
    print("Mission failed")
    
