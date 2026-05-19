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

    S = S/N
    print(f"ТУТ S {S}")
    for n in range(N):
        if matrix[m][n] < S:
            iterator += 1
    print(iterator)
    iterator = 0


