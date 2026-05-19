import random
from math import inf, sqrt
# ------- Заполнение массива
N = 10  # int(input('N '))
X = []
Y = []
for i in range(N):
    X.append(random.randint(1, 5))
    Y.append(random.randint(1, 5))
print(X, Y)
# ------- Заполнение массива

min_R = inf
Bx, By = int(input("Bx? ")), int(input("By? "))

for i in range(N):
    x, y = X[i], Y[i]

    R = sqrt((Bx - x) ** 2 + (By - y) ** 2)

    if R < min_R and R != 0:
        min_R = R
        print(f"({Bx}-{x})**2 + ({By}-{y})**2")
        
print(min_R)