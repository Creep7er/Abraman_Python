import random
from math import inf

# ------- Заполнение массива
N = 25
lst = []
for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива

lst = [1, 4, 3, 2, 2, 3, 4, 3, 2, 1, 0, -1, 3, 4]
print(lst)

count = 0
funArray = []
in_period = False
inc_or_dec = None  # True - возрастание, False - убывание

for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
        if not in_period:
            in_period = True
            inc_or_dec = True
            count += 1
        elif inc_or_dec == False:
            in_period = True
            inc_or_dec = True
            count += 1
    elif lst[i] < lst[i-1]:
        if not in_period:
            in_period = True
            inc_or_dec = False
            count += 1
        elif inc_or_dec == True:
            in_period = True
            inc_or_dec = False
            count += 1
    else: 
        in_period = False
        inc_or_dec = None
        
    if in_period:
        funArray.append(lst[i])

print(funArray)
print(count)