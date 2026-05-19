import random
from math import inf
# ------- Заполнение массива
N = 10 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 5))

print(lst)
print(len(lst))
# ------- Заполнение массива
i = 1

while i < len(lst):
    if lst[i] == lst[i-1]:
        lst.pop(i)
    else:
        i += 1


print(len(lst))
print(lst)
