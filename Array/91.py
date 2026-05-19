import random
from math import inf
# ------- Заполнение массива
N = 10 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 99))

print(lst)
# ------- Заполнение массива
K = int(input("K "))
L = int(input("L "))

kek = L - K

while kek >= 0:
    lst.pop(K)
    kek -= 1

print(len(lst))
print(lst)
