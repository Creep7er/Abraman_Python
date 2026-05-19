import random
# ------- Заполнение массива
N = int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 10))
print(A)

# ------- Заполнение массива

for i in A:
    if i % 2 != 0:
        NEchet = i

for i in range(len(A)):
    if A[i] % 2 != 0:
        A[i] = A[i] + NEchet

print(A)