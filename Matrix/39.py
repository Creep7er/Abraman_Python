from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    row.append(1)
    for n in range(1, N+1):
        row.append(random.randint(0, 100))
    matrix.append(row)
N += 1
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
arra = []
counter = 0
for n in range(N):
    flag = False
    for m in range(M):
        for m_1 in range(M):
            if matrix[m][n] != matrix[m_1][n]:
                counter += 1
                flag = True
                break
        if flag:
            break
print(counter)
        