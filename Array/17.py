import random
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива

print(lst)

left = 0
right = N - 1

while left <= right:

    for i in range(2):
        if left <= right:
            print(lst[left])
            left += 1

    for i in range(2):
        if left <= right:
            print(lst[right])
            right -= 1