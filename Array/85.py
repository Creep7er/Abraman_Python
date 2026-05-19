import random
from math import inf
# ------- Заполнение массива

N = int(input('N '))
K = int(input("K="))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 10))
print(lst)
lst =lst[-K:] + lst[:-K]
#вправо
lst = lst[K:]+lst[:K]
print(lst)
# # ------- Заполнение массива
# K = int(input('K '))
# maxs = -inf
# mins = inf
# add_arra = []
# print(lst)


# for m in range(len(lst)-1, len(lst)-K-1, -1):
#     add_arra.append(lst[m])
# for i in range(len(lst)-1, 0, -1):
#     lst[i] = lst[i-K] 

# for n in range(K):
#     lst[n] = add_arra[n]

# print(lst)