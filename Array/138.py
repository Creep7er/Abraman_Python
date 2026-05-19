import random
from math import inf, sqrt
# ------- Заполнение массива
N = 10  # int(input('N '))
X = []
Y = []
for i in range(N):
    X.append(random.randint(-5, 5))
    Y.append(random.randint(-5, 5))
print(X)
print(Y)
# ------- Заполнение массива
min_R = inf
sides = []

for i in range(len(X)):
    x1 = X[i]
    y1 = Y[i]

    for j in range(i+1, len(X)):
        x2 = X[j]
        y2 = Y[j]

        for k in range(j+1, len(X)):
            x3 = X[k]
            y3 = Y[k]
            R1 = sqrt((x1 - x2)**2 + (y1 - y2)**2)
            R2 = sqrt((x2 - x3)**2 + (y2 - y3)**2)
            R3 = sqrt((x3 - x1)**2 + (y3 - y1)**2)
            R_S = R1 + R2 + R3
            if min_R > R_S:
                min_R = R_S
                result = f"{X[i]}:{Y[i]}, {X[j]}:{Y[j]}, {X[k]}:{Y[k]}"



print(min_R, result)