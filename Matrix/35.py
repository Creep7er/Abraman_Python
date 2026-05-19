from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(-5, 5))
    matrix.append(row)
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
nechetnie = 0
nechet_n = 0
flag = False
for n in range(N):
    for m in range(M):
        if matrix[m][n] % 2 != 0:
            nechetnie = n
        else:
            nechetnie = 0
            break
    if nechetnie:
        nechet_n = n
        break

if nechet_n:
    print(nechet_n+1)
    for m in range(M):
        print(matrix[m][nechet_n])
else:
    print("Mission failed")
    
