import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 99))
print(A)

# ------- Заполнение массива

maxs = -inf
mins = inf

min_cord = 0
max_cord = 0


for i in range(len(A)):
    if A[i] <= mins:
        mins = A[i]
        min_cord = i
    if A[i] >= maxs:
        maxs = A[i]
        max_cord = i

print(maxs, mins, max_cord, min_cord)

if max_cord < min_cord:
    max_cord, min_cord = min_cord, max_cord
print(min_cord+1, max_cord+1)
for j in range(min_cord+1, max_cord):
    A[j] = 0

print(A)
