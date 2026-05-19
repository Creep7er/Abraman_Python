from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    kek = random.randint(0, 100)
    if random.randint(0,1):  
        for n in range(1, N+1):
            row.append(kek + n)
    else:
        for n in range(1, N+1):
            row.append(random.randint(0, 100))
    matrix.append(row)
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
flag = False
counter = 0
for m in range(M):
    for n in range(1, N):
        if matrix[m][n-1] < matrix[m][n]:
            flag = True
        else:
            flag = False
            break
    if flag:
        counter += 1

print(counter)