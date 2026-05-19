import random
from math import inf
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива

print(lst)
maxs = -inf
for i in range(1, N, 2):
    if lst[i] > maxs:
        maxs = lst[i]


print(maxs)