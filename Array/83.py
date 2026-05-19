import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 10))


# ------- Заполнение массива
maxs = -inf
mins = inf

print(lst)
kek = lst[-1]

for i in range(len(lst)-1, 0, -1):
    lst[i] = lst[i-1]
lst[0] = kek

print(lst)