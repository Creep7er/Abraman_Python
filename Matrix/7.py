M = int(input("M? "))
N = int(input("N? "))
K = int(input("K? ")) - 1
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(10*n + m)
    matrix.append(row)

for m in range(M):
    print(matrix[m])

print("K-ая строка", matrix[K])
