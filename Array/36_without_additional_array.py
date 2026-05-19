import random
from math import inf
# ------- Заполнение массива
N = 25 #int(input(''))

#lst = [1, 2, 1, 2, 1, 2, 1, 2, 1]
#lst.append(1000)
for _ in range(N):
   lst.append(random.randint(1, 99))
#lst.append(999)
# ------- Заполнение массива

maxs = -inf
print(lst)

def maximus(i):
    global maxs
    if i > maxs:
        maxs = i
        print(maxs)
flag = 0
for i in range(len(lst)):
    if i != 0 and i != len(lst)-1:
        if not (lst[i - 1] > lst[i] and lst[i] < lst[i + 1] or lst[i - 1] < lst[i] and lst[i] > lst[i + 1]):
            flag = 1
            maximus(lst[i])
    else:
        maximus(lst[i])


if flag:
    print(maxs)
else: print(flag)