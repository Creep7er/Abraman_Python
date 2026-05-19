import random
from math import inf, sqrt
# ------- Заполнение массива
N_1 = 10  # int(input('N '))
N_2 = 12

A_X = []
A_Y = []
for i in range(N_1):
    A_X.append(random.randint(-5, 5))
    A_Y.append(random.randint(-5, 5))
print(A_X, A_Y)
B_X = []
B_Y = []
for i in range(N_2):
    B_X.append(random.randint(-50, 50))
    B_Y.append(random.randint(-50, 50))
print(B_X, B_Y)
# ------- Заполнение массива
min_R = inf
for i in range(N_1):
    x1 = A_X[i]
    y1 = A_Y[i]

    for j in range(N_2):
        x2 = B_X[j]
        y2 = B_Y[j]

        R = sqrt((x1 - x2)**2 + (y1 - y2)**2)

        if R < min_R:
            min_R = R
            tochka1 = f"{x1}:{y1}"
            tochka2 = f"{x2}:{y2}"
print(min_R, f"({tochka1}, {tochka2})")