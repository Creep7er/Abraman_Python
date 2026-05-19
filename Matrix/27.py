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
mins = inf
min_list = []
for m in range(M):
    for n in range(N):
        if matrix[m][n] < mins:
            mins = matrix[m][n]

    min_list.append(mins)
    mins = inf
print(min_list)
max_among_list = -inf

for i in min_list:
    if i > max_among_list:
        max_among_list = i

print(max_among_list)
