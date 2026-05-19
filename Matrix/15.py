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
for m in range(M):
    for i in range(m, M-m):
        print(matrix[m][i])
        i1 = i
    for x in range(m+1, M-m):
        print(matrix[x][i1])
        x1 = x
    for i in range(M-m-2, m-1, -1):
        print(matrix[x1][i])
        i1 = i
    for x in range(M-m-2, m, -1):
        print(matrix[x][i1])
