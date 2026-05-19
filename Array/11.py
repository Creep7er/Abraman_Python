import random
# ------- Заполнение массива
N = int(input(''))

lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))
# ------- Заполнение массива
K = int(input('K '))
"""print(lst)
for i in range(1, N+2):
    try:
        print(lst[i*K])
    except IndexError:
        break
"""

for x in range(0, N, K):
    print(lst[x])