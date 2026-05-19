import random
from math import inf, sqrt
# ------- Заполнение массива
N = 10  # int(input('N '))
X = []
Y = []
for i in range(N):
    X.append(random.randint(-50, 50))
    Y.append(random.randint(-50, 50))
print(X, Y)
# ------- Заполнение массива
max_R = inf
min_y = 0
min_x = 0
for i in range(len(X)):
    x = X[i]
    y = Y[i]

    if (x > 0 and y > 0) or (x < 0 and y < 0):
        R = sqrt(x**2 + y**2)
        if R < max_R:
            max_R = R
            min_x = x
            min_y = y
print(max_R, f"({min_x};{min_y})")