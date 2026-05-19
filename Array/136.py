import random
from math import inf, sqrt
# ------- Заполнение массива
N = 10  # int(input('N '))
X = []
Y = []
for i in range(N):
    X.append(random.randint(-5, 5))
    Y.append(random.randint(-5, 5))
print(X, Y)
# ------- Заполнение массива
min_R = inf

for i in range(len(X)):
    x1 = X[i]
    y1 = Y[i]

    for j in range(len(X)):
        x2 = X[j]
        y2 = Y[j]

        if i != j:
            R = sqrt((x1 - x2)**2 + (y1 - y2)**2)

            if R < min_R:
                min_R = R
                tochka1 = f"{x1}:{y1}"
                tochka2 = f"{x2}:{y2}"
print(min_R, f"({tochka1}, {tochka2})")