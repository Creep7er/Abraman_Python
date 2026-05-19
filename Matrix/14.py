M = int(input("M? "))
matrix = []

for i in range(1, M + 1):
    row = []
    for j in range(1, M + 1):
        row.append(j * 10 + i)
    matrix.append(row)

print("Матрица")
for row in matrix:
    print(row)

print("Ответ")

for k in range(M):
    # столбец k
    for i in range(k, M - k):
        print(matrix[i][k])
    # нижняя строка
    for j in range(k + 1, M - k):
        print(matrix[M - k - 1][j], end=' ')
    print()