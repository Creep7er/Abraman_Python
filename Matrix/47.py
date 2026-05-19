from math import inf
import random
K_1 = int(input("K1? "))
K_2 =int(input("K2? "))
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(0, 100))
    matrix.append(row)

print("Матрица")
for m in range(M):
    print(matrix[m])

print("Ответ")
k1 = matrix[K_1-1]
k2 = matrix[K_2-1]
matrix.pop(K_1-1)
matrix.insert(K_1-1, k2)
matrix.pop(K_2-1)
matrix.insert(K_2-1, k1)

for m in range(M):
    print(matrix[m])


    