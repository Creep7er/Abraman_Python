import random
from math import inf, sqrt
# ------- Заполнение массива
N = 5  # int(input('N '))
X = []
Y = []
for i in range(N):
    X.append(random.randint(-5, 5))
    Y.append(random.randint(-5, 5))
print(X)
print(Y)
# ------- Заполнение массива

for i in range(len(X)):
    for j in range(i+1, len(X)):
        if X[i] + Y[i] < X[j] + Y[j]:
            X[i], X[j] = X[j], X[i]
            Y[i], Y[j] = Y[j], Y[i]
        elif X[i] + Y[i] == X[j] + Y[j]:
            if X[i] < X[j]:
                X[i], X[j] = X[j], X[i]
                Y[i], Y[j] = Y[j], Y[i]

print(X)
print(Y)