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

K = int(input("K"))

lst.insert(K-1, 0)

print(lst)
print(len(lst))