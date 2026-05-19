import random
from math import inf

# ------- Заполнение массива
N = int(input(''))
lst = []
for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
R = int(input(''))
print(lst)

count = 0
arra = []
maxs = -inf

for i in range(len(lst)):
    check = abs(lst[i] - R)
    if check < maxs:
        maxs = check
        closest = lst[i]

print(closest)