import random
from math import inf

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

matrix2 = []
for m in range(M):
    row = []
    for n in range(N):
        row.append(matrix[m][n])
    matrix2.append(row)

print("Ответ")
for m in range(M):
    for n in range(N):
        flag = True

        for m_1 in range(-1, 2):
            for n_1 in range(-1, 2):
                if m_1 == 0 and n_1 == 0:
                    continue

                m2 = m + m_1
                n2 = n + n_1

                if 0 <= m2 < M and 0 <= n2 < N:
                    if matrix[m][n] <= matrix[m2][n2]:
                        flag = False

        if flag:
            matrix2[m][n] = -matrix2[m][n]

for m in range(M):
    print(matrix2[m])