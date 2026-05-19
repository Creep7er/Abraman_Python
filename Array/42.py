import random
from math import inf

# ------- Заполнение массива
N = int(input(''))
lst = []
for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
print(lst)

maxs = -inf
count = 0 

for i in range(len(lst)-1):
    a = lst[i] + lst[i+1]
    if a > maxs:
        maxs = a
        count = i

arra = [lst[count], lst[count+1]]
print(arra)