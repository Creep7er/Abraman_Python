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
kek = lst[0]

for i in range(1, len(lst)):
    lst[i-1] = lst[i]
lst[-1] = kek

print(lst)