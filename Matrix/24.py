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
maxs = -inf
for m in range(M):
    for n in range(N):
        if matrix[m][n] > maxs:
            maxs = matrix[m][n]
    print(maxs)
    maxs = -inf
