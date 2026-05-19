M = int(input("M? "))
N = int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(10*n + m)
    matrix.append(row)
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
for m in range(M):
    for K in range(1, N, 2):
        print(matrix[m][K], end=" ")
    print()