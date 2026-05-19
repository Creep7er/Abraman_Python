import random
# ------- Заполнение массива
N = int(input('N: '))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
K = int(input('K: '))
L = int(input('L: '))
SUM = 0

print(lst)
for i in range(K, L+1): # Спросить правильно ли тут
    SUM += lst[i]
    print(SUM)
print(SUM)