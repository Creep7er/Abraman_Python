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
mins = inf
max_n = 0
for n in range(N):
    for m in range(M):
        P *= matrix[m][n]
    if mins > P:
        mins = P
        max_n = n
    P = 1
print(max_n, mins)
