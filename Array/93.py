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
i = len(lst)-2

ANS = []

while i >= 2:
    lst.pop(i)
    i -= 2


print(len(lst))
print(lst)
