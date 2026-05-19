import random
# ------- Заполнение массива
N = 10 #int(input('N: '))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
print(lst)
for x in range(N-1, 0, -1):
    if lst[1] < lst[x] < lst[N-1]:
        ANS = x
        break
    else: ANS = 0

print(ANS)
if ANS != 0: print(lst[ANS])