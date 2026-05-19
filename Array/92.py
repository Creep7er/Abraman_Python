import random
from math import inf
# ------- Заполнение массива
N = 10 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))

print(lst)
print(len(lst))
# ------- Заполнение массива
i = 0

ANS = []

while i < len(lst):
    if lst[i] % 2 != 0:
        lst.pop(i)
    else:
        i += 1


print(len(lst))
print(lst)
