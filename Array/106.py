import random
# ------- Заполнение массива
N = 10 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 10))

print(lst)
print(len(lst))
# ------- Заполнение массива

i = (len(lst) - 1) - ((len(lst) - 1) % 2)

while i >= 2:
    lst.insert(i + 1, lst[i])
    i -= 2

print(lst)
print(len(lst))