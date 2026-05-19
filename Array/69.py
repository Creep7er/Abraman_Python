import random
from math import inf
# ------- Заполнение массива
N = int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 10))
print(A)

# ------- Заполнение массива

for i in range(0, len(A), 2):
    kek = A[i] 
    A[i] = A[i+1] 
    A[i+1] = kek

print(A)