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
count = 0
SUM = 0
for i in range(N):
    if not (K <= i+1 <= L):
        SUM += lst[i]
        count += 1

print(SUM/count)
print(f'{SUM} / {count}')