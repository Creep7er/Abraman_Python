M = int(input("M? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, M+1):
        row.append(10*n + m)
    matrix.append(row)
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
for k in range(M):
    # строка k
    for j in range(k, M - k):
        print(matrix[k][j], end=' ')
    print()

    # правый столбец
    for i in range(k + 1, M - k):
        print(matrix[i][M - k - 1])