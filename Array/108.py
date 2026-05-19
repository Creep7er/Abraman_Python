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
    if lst[i] > 0:
        lst.insert(i, 0)
        i += 1
    i += 1

print(lst)
print(len(lst))