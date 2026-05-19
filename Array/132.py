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
max_R = 0
max_y = 0
max_x = 0
for i in range(len(X)):
    x = X[i]
    y = Y[i]

    if x > 0 and y > 0:
        R = sqrt(x**2 + y**2)
        if R > max_R:
            max_R = R
            max_x = x
            max_y = y
print(max_R, f"({max_x};{max_y})")