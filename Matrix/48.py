from math import inf
import random
K_1 = int(input("K1? "))-1
K_2 =int(input("K2? "))-1
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


for m in range(M):
    matrix[m][K_1], matrix[m][K_2] = matrix[m][K_2], matrix[m][K_1]
for m in range(M):
    print(matrix[m])


    