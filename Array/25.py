import random
# ------- Заполнение массива
N = int(input('N: '))
lst = []

while len(lst) < N:
    num = random.randint(1, 99)
    if num not in lst:  # проверка на уникальность
        lst.append(num)
# ------- Заполнение массива
#lst = [2, 4, 8, 16, 32, 64, 128]
q = lst[1] / lst[0]

print(lst)
count = 0
SUM = 0
for i in range(2, len(lst)):
    if lst[i] / lst[i-1] == q:
        ANS = q
    else: ANS = 0

print(ANS)