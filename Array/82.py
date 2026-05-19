import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 10))


# ------- Заполнение массива 
K = int(input('K '))
maxs = -inf
mins = inf
print(lst)

for i in range(K, len(lst)):
    lst[i-K] = lst[i]
    print(i)


for m in range(len(lst)-1, len(lst)-K-1, -1):
    lst[m] = 0

print(lst)


