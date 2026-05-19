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


first_n = []
for n in range(N):
    first_n.append(matrix[0][n])
n_mas = []
flag = 0
for n in range(1, N):
    for m in range(M):
        n_mas.append(matrix[m][n])
    if n_mas == first_n:
        flag += 1
        n_mas = []
    else:
        n_mas = []
        
        
if flag:
    print(f"{flag} - наш ответ") 
else:
    print("Нет похожих")
