import random
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива

ANSWER = []
for i in range(N):
    if lst[i] % 2 != 0:
        ANSWER.append(lst[i])
print("Первоначальный массив", lst)
print("Ответ на задачу", ANSWER)