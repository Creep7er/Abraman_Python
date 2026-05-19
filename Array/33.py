import random
from math import inf
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
count = 0
print(lst)

for i in range(1, N-1):
    if lst[i - 1] < lst[i] and lst[i] > lst[i + 1]:
        ANS = i
        break
        


print(ANS, lst[ANS])