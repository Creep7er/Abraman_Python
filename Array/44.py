import random

# ------- Заполнение массива
N = int(input(''))
lst = []
for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
lst = [5, 3, 8, 3, 1, 7]
print(lst)

first_index = -1
second_index = -1

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            first_index = i
            second_index = j
            break
    if first_index != -1:
        break

print(first_index, second_index)