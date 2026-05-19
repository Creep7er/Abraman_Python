import random
from math import inf
# ------- Заполнение массива
N = 10 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 5))

print(lst)
print(len(lst))
# ------- Заполнение массива

i = len(lst)-1
counter = 1

while i >= 0:
    j = len(lst) - 1
    counter = lst.count(lst[i])
    while j >= 0:
        if lst[i] == lst[j]:
            counter += 1
        j -= 1
    # print(counter, lst[i])        
    if counter < 3:
        lst.pop(i)
                
    i -= 1


print(len(lst))
print(lst)
