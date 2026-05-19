from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []


for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(0, 100))
    matrix.append(row)
#matrix.append(row_1)
#M += 2
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
max_count = 0
counter = 0

for m in range(M):
    row_max = 0
    
    for n in range(N):
        count = 0
        
        for n_1 in range(N):
            if matrix[m][n] == matrix[m][n_1]:
                count += 1
        
        if count > row_max:
            row_max = count
    
    if row_max >= max_count:
        max_count = row_max
        counter = m

print(counter+1)