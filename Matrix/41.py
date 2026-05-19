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
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")
max_count = 0
counter = 0

for n in range(N):
    col_max = 0
    
    for m in range(M):
        count = 0
        
        for m_1 in range(M):
            if matrix[m][n] == matrix[m_1][n]:
                count += 1
        
        if count > col_max:
            col_max = count
    

    if col_max > max_count:
        max_count = col_max
        counter = n
print(counter+1)