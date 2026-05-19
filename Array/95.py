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

while i > 0:
    if lst[i] == lst[i-1]:
        lst.pop(i)
    i -= 1


print(len(lst))
print(lst)
