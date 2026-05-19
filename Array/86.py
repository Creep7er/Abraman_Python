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
add_arra = []
print(lst)

for m in range(K-1, -1, -1):
    add_arra.append(lst[m])

print(add_arra)
for i in range(K, len(lst)):
    lst[i-K] = lst[i]

for n in range(1, K+1):
    lst[-n] = add_arra[n-1]

print(lst)