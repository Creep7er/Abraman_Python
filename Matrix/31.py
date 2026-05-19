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
iterator = 0
for m in range(M):
    for n in range(N):
        S += matrix[m][n]

S = S/(N*M)
print("S = ", S)
bliz = inf
bliz_n = 0
bliz_m = 0
for m in range(M):
    for n in range(N):
        if abs(S - matrix[m][n]) < bliz:
            bliz = abs(S - matrix[m][n])
            bliz_n = n
            bliz_m = m

print(bliz_n, bliz_m, matrix[bliz_m][bliz_n])




