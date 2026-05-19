import random
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
print(lst)
for x in range(2, N, 2):
    print(lst[x])
for i in range(1, N, 2):
    print(lst[i])

# такой же способ без range print(*lst[0::2])