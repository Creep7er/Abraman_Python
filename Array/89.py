import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))

lst.sort(reverse=True)

lst.insert(random.randint(0, N-1), random.randint(-99,99))

print(lst)
# ------- Заполнение массива
maxs = -inf
mins = inf
izgoy = 0

for i in range(1, len(lst)):
    if (lst[i-1] <= lst[i-2] and lst[i-1] <= lst[i]) or (lst[i-1] <= lst[i]):
        izgoy = i-1
        break


print(lst[izgoy])

for i in range(len(lst)):
    if lst[izgoy] <= lst[-1]:
        lst.append(lst[izgoy])
        lst.pop(izgoy)
        break
    if lst[i-1] <= lst[izgoy] and lst[izgoy] >= lst[i]:
        lst.insert(i-1, lst[izgoy])
        lst.pop(izgoy)
        break


print(lst)