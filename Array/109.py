import random
# ------- Заполнение массива
N = 10 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(-50, 50))

print(lst)
print(len(lst))
# ------- Заполнение массива
i = 1
while i < len(lst):
    if lst[i-1] < 0:
        lst.insert(i, 0)
        i += 1
    i += 1

print(lst)
print(len(lst))