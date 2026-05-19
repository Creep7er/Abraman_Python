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

for i in range(len(X)):
    x1 = X[i]
    y1 = Y[i]

    for j in range(len(X)):
        x2 = X[j]
        y2 = Y[j]
        if x1 > x2:
            kekich_x = X[i]
            X[i]= X[j]
            X[j] = kekich_x
            kekich_y = Y[j]
            Y[i] = Y[j]
            Y[j] = kekich_y
        if x1 == x2:
            if y1 < y2:
                kekich_x = X[i]
                X[i]= X[j]
                X[j] = kekich_x
                kekich_y = Y[j]
                Y[i] = Y[j]
                Y[j] = kekich_y    

print(X)
print(Y)