from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(0, 100))
    row_1 = row
    matrix.append(row)
    
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
arra = []
counter = 0
for m in range(M):
    arra = []
    flag = False
    kekich = set(matrix[m])
    if kekich != M:
        counter += 1
print(counter)
        