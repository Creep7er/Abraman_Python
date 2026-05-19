import random
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(-99, 99))
# ------- Заполнение массива

print(lst)

for i in range(1, N):
    if lst[i] > 0 and lst[i-1] < 0 or lst[i] < 0 and lst[i-1] > 0:
        ANS = 0
    else:
        ANS = i
        break

print(ANS)