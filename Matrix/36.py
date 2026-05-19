from math import inf
import random
M = 6 #int(input("M? "))
N = 6 #int(input("N? "))
matrix = []

for m in range(1, M+1):
    row = []
    for n in range(1, N+1):
        row.append(random.randint(0, 1))#100))
    matrix.append(row)
print("Матрица")
for m in range(M):
    print(matrix[m])
print("Ответ")


first_m = matrix[0]
flag = 0
for m in range(1, M):
    if matrix[m] == first_m:
        flag += 1
        print(matrix[m])
        
        
if flag:
    print(f"{flag} - наш ответ") 
else:
    print("Нет похожих")





