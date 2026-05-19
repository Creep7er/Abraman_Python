import random
from math import inf
# ------- Заполнение массива
N = 10 #int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
count = 0
ANS = []
maxs = -inf
print(lst)
ANS.append(lst[0])
for i in range(1, N-1):
    if not (lst[i - 1] > lst[i] and lst[i] < lst[i + 1] or lst[i - 1] < lst[i] and lst[i] > lst[i + 1]):
        ANS.append(lst[i])
        break
ANS.append(lst[-1])
print(ANS)
for i in range(len(ANS)):
    if ANS[i] > maxs:
        maxs = ANS[i]
        

if ANS:
    print(maxs)
else: print(0)