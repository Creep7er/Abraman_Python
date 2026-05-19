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
maxs = -inf
min_list = []
for n in range(N):
    for m in range(M):
        if matrix[m][n] > maxs:
            maxs = matrix[m][n]

    min_list.append(maxs)
    maxs = -inf
print(min_list)
min_among_list = inf

for i in min_list:
    if i < min_among_list:
        min_among_list = i

print(min_among_list)
