import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 10))
print(lst)

# ------- Заполнение массива
ANS = []
maxs = -inf
mins = inf

for i in range(1, len(lst)-1):
    ANS.append(((lst[i - 1] + lst[i] + lst[i+1])/3))

print(ANS)
