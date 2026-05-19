import random
from math import inf
# ------- Заполнение массива
N = int(input(''))
lst = []
for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
print(lst)

first_index = -1
second_index = -1
mins = inf
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if abs(lst[i] - lst[j]) <= mins:
            mins = abs(lst[i] - lst[j])
            first_index = i
            second_index = j       

print(first_index, lst[first_index], second_index, lst[second_index])