import random
from math import inf
# ------- Заполнение массива
N = 10 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 5))

lst = [1, 3, 5, 12, 1, 3, 1, 12]
print(lst)
print(len(lst))
# ------- Заполнение массива

maxs = -inf
mins = inf

for i in range(1, len(lst)):
    if lst[i] >= maxs:
        maxs = lst[i]
    if lst[i] <= mins:
        mins = lst[i]

i = 0
while i < len(lst):
    if lst[i] == mins:
        lst.insert(i, 0)
        i += 1
    i += 1

i = 0
while i < len(lst):
    if lst[i] == maxs:
        lst.insert(i+1, 0)
        i += 1
    i += 1
print(lst)
print(len(lst))