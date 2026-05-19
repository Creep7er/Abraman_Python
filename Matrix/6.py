import random
M = int(input("M? "))
N = int(input("N? "))
D = int(input("D?" ))

# =====
lst = []
for _ in range(M):
    lst.append(random.randint(-99, 99))

print("Исходный", lst)
# =====
matrix = []

for m in range(M):
    row = []
    row.append(lst[m])
    for n in range(N):
        row.append(row[n] * D)
    matrix.append(row)

for m in range(M):
    print(matrix[m])
