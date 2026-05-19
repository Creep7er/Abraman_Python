import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))

lst.sort()

lst.insert(0, random.randint(1,99))

print(lst)
# ------- Заполнение массива
maxs = -inf
mins = inf

for i in range(len(lst)):
    if lst[i] >= lst[0] and lst[0] <= lst[i+1]:
        lst.insert(i, lst[0])
        lst.pop(0)
        break


print(lst)