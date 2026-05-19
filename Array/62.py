import random
# ------- Заполнение массива
N = int(input(''))
A = []

for _ in range(N):
    A.append(random.randint(-10, 10))

# ------- Заполнение массива
print(A)
B = [] #Положительные
C = [] #Отрицательные
for i in A:
    if i > 0:
        B.append(i)
    if i < 0:
        C.append(i)

print(B, C)