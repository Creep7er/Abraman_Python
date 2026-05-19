import random

# ------- Заполнение массива
N = 10
lst = []

for _ in range(N):
    lst.append(random.randint(1, 10))

print(lst)
print(len(lst))
# ------- Заполнение массива

# Находим последний нечетный индекс
i = (len(lst) - 1) - ((len(lst)) % 2)

while i >= 1:
    lst.insert(i + 1, lst[i])
    i -= 2

print(lst)
print(len(lst))