import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(-99, 99))
print(lst)

# ------- Заполнение массива
ANS = []
maxs = -inf
mins = inf

for i in range(1, N-1):
    if lst[i - 1] > lst[i] and lst[i] < lst[i + 1]:
        ANS.append(i)

for n in ANS:
    lst[n] = (lst[n])**2

print(lst)
