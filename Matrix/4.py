import random
M = int(input("M? "))
N = int(input("N? "))


# =====
lst = []
for _ in range(N):
    lst.append(random.randint(-99, 99))

print("Исходный", lst)
# =====
matrix = []

for m in range(M):
    row = []
    for n in range(N):
        row.append(lst[n])
    matrix.append(row)

for m in range(M):
    print(matrix[m])
