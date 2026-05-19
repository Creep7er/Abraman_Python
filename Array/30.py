import random
from math import inf
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
ANS = []
count = 0
print(lst)

for i in range(N - 1):
    if lst[i] > lst[i + 1]:
        ANS.append(i)
        count += 1


print(ANS, count) # вместо count можно len(ANS)