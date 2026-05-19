M = int(input("M? "))
N = int(input("N? "))
K = int(input("K? "))-1
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
for i in range(N):
    S += matrix[K][i]
    P *= matrix[K][i]

print(S, P)
