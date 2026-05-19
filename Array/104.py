import random
# ------- Заполнение массива
N = 10 #int(input('N '))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 5))

print(lst)
print(len(lst))
# ------- Заполнение массива

K = int(input("K "))
M = int(input("M "))

i = 0
while i < M:
    lst.insert(K-1, 0)
    i += 1

print(lst)
print(len(lst))