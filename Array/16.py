import random
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
print(lst)
for i in range(1, N):
    print(f"{i}:", lst[i])
    print(f"{i}:", lst[N-i])