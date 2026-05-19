import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 10))
print(lst)

# ------- Заполнение массива

maxs = -inf
mins = inf

for i in range(1, len(lst)):
    lst[i-1] = lst[i] 
lst[len(lst)-1] = 0
print(lst)
