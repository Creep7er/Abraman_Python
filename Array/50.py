import random
from math import inf

# ---- Создание массива
N = int(input())

lst = []

for x in range(N):
    lst.append(x)
random.shuffle(lst)
# ---- Создание массива
print(lst)
ANS = 0
for i in range(1, N-1):
    if lst[i-1] > lst[i]:
        ANS+=1

print(ANS)