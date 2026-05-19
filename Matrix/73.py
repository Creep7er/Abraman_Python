from math import inf
import random
K = 2 #int(input("K? ")) - 1
M = 5 #int(input("M? "))
N = 5 #int(input("N? "))
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
cord = 0
for n in range(N):
    for m in range(M):
        if matrix[m][n] < 0:
           flag = True
           cord = n
        else: flag = False; break
if flag:
    for m_1 in range(M):
        matrix[m_1].insert(cord+1, 0)

if flag: print('изменено')
for m in range(M):
    print(matrix[m])
