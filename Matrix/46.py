from math import inf
import random

M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(0, 100))
    matrix.append(row)

print("Матрица")
for m in range(M):
    print(matrix[m])

print("Ответ")

flag = 0

for m in range(M):
    max_n = -inf
    max_n_cord = 0

    for n in range(N):
        if matrix[m][n] > max_n:
            max_n = matrix[m][n]
            max_n_cord = n

    min_m = inf
    min_m_cord = 0

    for m_1 in range(M):
        if matrix[m_1][max_n_cord] < min_m:
            min_m = matrix[m_1][max_n_cord]
            min_m_cord = m_1

    if min_m == max_n:
        flag = min_m
        break

if flag != 0:
    print(f"{flag} - наш ответ") 
else:
    print("Нет похожих")