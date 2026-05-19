import random
from math import inf
# --- СОЗДАЕМ МАССИВ
N = int(input("N "))
lst = []
for _ in range(N):
    lst.append(random.randint(1, 10))
print(lst)
# ---- НЕ ЩУПАТЬ ДО СЮДА
mins = inf

for i in range(len(lst)):
    if lst[i] < mins:
        mins = lst[i]
        min_index = i

print(mins, min_index)

min_position = []
for x in lst:
    if x == mins:
        lst.remove(x)
        min_position.append(x)

for i in range(min_index-1):
    for j in range(min_index-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for i in range(min_index-1, -1):
    for j in range(-1):
        if lst[j] < lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for n in min_position:
    lst.insert(n, mins)

print(lst)

    