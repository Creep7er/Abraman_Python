import random
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива

print(lst)

for i in range(N-1):
    if lst[i] % 2 == lst[i-1] % 2:
        ANS = i
        break

print(ANS)