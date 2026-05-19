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
#print(matrix[0])
for m in range(0, M, 2):
    for x in range(N):
        print(matrix[m][x], end=" ")
    print()
    if not(m == M-1):
        for x in range(N-1, -1, -1):
            print(matrix[m+1][x], end=" ")
    print()