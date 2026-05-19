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

for i in range(len(lst)-1, 0, -1):
    print(i)
    lst[i] = lst[i-K] 


for m in range(0, K):
    lst[m] = 0

print(lst)


