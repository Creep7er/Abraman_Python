import random
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
print(lst)
for i in range(1, N, 2):
    print(lst[i])
for x in range(N-2, 0, -2):
    print(lst[x])