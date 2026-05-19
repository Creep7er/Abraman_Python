import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []
for _ in range(N):
    lst.append(random.randint(1, 10))
# ------- Заполнение массива
R = int(input('R '))

print(lst)

closest_i = -1
closet_j = -1
mins = inf
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        check = abs((lst[i] + lst[j]) - R)
        if check < mins:
            mins = check
            closest_i = i
            closet_j = j
print(closest_i, lst[closest_i], closet_j, lst[closet_j])