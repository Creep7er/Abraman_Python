import random
from math import inf, sqrt
# ------- Заполнение массива
N = 10  # int(input('N '))
X = []
Y = []
for i in range(N):
    X.append(random.randint(-5, 5))
    Y.append(random.randint(-5, 5))
X = [0, 2, 5, 1, 5, -2, 4, -5, -2, -2]
Y = [0, -1, -4, -5, -4, -4, 1, 0, 1, 2]
print(X)
print(Y)
# ------- Заполнение массива

for i in range(len(X)):
    for j in range(i+1, len(X)):
        if X[i] > X[j]:
            X[i], X[j] = X[j], X[i]
            Y[i], Y[j] = Y[j], Y[i]
        elif X[i] == X[j]:
            if Y[i] > Y[j]:
                X[i], X[j] = X[j], X[i]
                Y[i], Y[j] = Y[j], Y[i]

print(X)
print(Y)