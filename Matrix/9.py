M = int(input("M? "))
N = int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(10*n + m)
    matrix.append(row)
print("Исходная матрица")
for m in range(M):
    print(matrix[m])

print("ОТввет")
for m in range(0, M, 2):
    print(matrix[m])