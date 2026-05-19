import random
# ------- Заполнение массива
N = 10 #int(input('K: '))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
print(lst)
for x in range(N):
    if lst[x] < lst[N-1]:
        ANS = lst[x]
        break
    else: ANS = 0

print(ANS)