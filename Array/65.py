import random
# ------- Заполнение массива
N = int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 10))
print(A)

# ------- Заполнение массива

K = int(input('K '))
J = A[K]
for i in range(len(A)):
    A[i] = A[i] + J

print(A)