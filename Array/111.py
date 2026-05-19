import random
# ------- Заполнение массива
N = 10 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(-50, 50))

print(lst)
print(len(lst))
# ------- Заполнение массива
i = 0
while i < len(lst):
    if lst[i] % 2 != 0:
        lst.insert(i, lst[i])
        lst.insert(i, lst[i])
        i += 2
    i += 1

print(lst)
print(len(lst))