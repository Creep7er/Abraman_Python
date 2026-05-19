from math import inf
import random
K = 2 -1 #int(input("K? ")) - 1
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
min_el = inf
min_cord = 0
for n in range(N):
    for m in range(M):
        if matrix[m][n] > 0:
            flag = True
        else: flag = False; break
        
    if flag:
        for m_1 in range(M):
            matrix[m_1].pop(n)
        N -=1
        break
if flag: print("изменено")
for m in range(M):
    print(matrix[m])
