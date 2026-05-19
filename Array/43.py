import random
# ------- Заполнение массива
N = int(input(''))
lst = []
for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива

lst = [9, 9, 7, 5, 5, 5, 3, 1, 1]
print(lst)

count = 1 
for i in range(1, len(lst)):
    if lst[i] != lst[i-1]:  
        count += 1

print(count)
