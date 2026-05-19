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
i = len(lst)-1

while i >= 0:
    j = len(lst)-1
    while j > i:
        if lst[i] == lst[j]:
            lst.pop(j)
        j -= 1
    i -= 1


print(len(lst))
print(lst)
