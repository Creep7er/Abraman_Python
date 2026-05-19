import random
from math import inf

# ---- Создание массива
N = int(input())

lst = []

for _ in range(N):
    lst.append(random.randint(1, N))

# ---- Создание массива
print(lst)
ANS = 0
for i in range(1, N-1):
    if i not in lst:
        ANS = i
        break

print(ANS)