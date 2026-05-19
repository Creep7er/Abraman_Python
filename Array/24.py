import random
# ------- Заполнение массива
N = int(input('N: '))
lst = []

while len(lst) < N:
    num = random.randint(1, 99)
    if num not in lst:  # проверка на уникальность
        lst.append(num)
# ------- Заполнение массива
#N = 10
#lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
d = lst[1] - lst[0]

print(lst)
count = 0
SUM = 0
for i in range(2, len(lst)):
    if lst[i] - lst[i-1] == d:
        ANS = d
    else: ANS = 0

print(ANS)