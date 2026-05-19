import random
# ------- Заполнение массива
N = int(input('N: '))
lst = []
for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива

K = int(input('K: '))
L = int(input('L: '))

print(lst)

SUM = 0
for i in range(N):
    if not (K <= i+1 <= L):
        SUM += lst[i]

print(SUM)