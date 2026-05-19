from math import inf

M = 5 #int(input("M? "))
N = 5 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(n + m)
    matrix.append(row)
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
S = 0
P = 1
maxs = -inf
max_m = 0
for m in range(M):
    for n in range(N):
        S += matrix[m][n]
    if maxs < S:
        maxs = S
        max_m = m
    S = 0
print(max_m, maxs)
