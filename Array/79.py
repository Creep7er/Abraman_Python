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

for i in range(len(lst)-1, 0, -1):
    if i == len(lst):
        lst.append(lst[i])
    else:
        lst[i] = lst[i-1] 
lst[0] = 0 
print(lst)
