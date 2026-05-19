import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))

lst.sort()

lst.append(random.randint(-99,99))

print(lst)
# ------- Заполнение массива
maxs = -inf
mins = inf

for i in range(len(lst)):
    if lst[-1] >= lst[-2]:
        break

    if lst[i] >= lst[-1] and lst[-1] <= lst[i+1]:
        lst.insert(i, lst[-1])
        lst.pop(-1)
        break


print(lst)