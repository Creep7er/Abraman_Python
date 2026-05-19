import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))

print(lst)
# ------- Заполнение массива
K = int(input("K" ))

lst.pop(K)

print(lst)
