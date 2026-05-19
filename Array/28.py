import random
from math import inf
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива

print(lst)
mins = inf
for i in range(2, N, 2):
    if lst[i] < mins:
        mins = lst[i]


print(mins)