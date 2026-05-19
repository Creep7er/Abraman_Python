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
for n in range(0, N, 2):
    for m in range(M):
        print(matrix[m][n])
    print()
    if n % 2 == 0 and n != N-1:
        for m in range(M-1, -1, -1):
            print(matrix[m][n+1])
        print()