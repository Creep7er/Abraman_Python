import random

N_A = int(input("N_A "))
N_B = int(input("N_B "))
N_C = int(input("N_C "))


A = []
B = []
C = []
for _ in range(N_A):
    A.append(random.randint(1, 10))
for _ in range(N_B):
    B.append(random.randint(1, 10))

for _ in range(N_C):
    C.append(random.randint(1, 10))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
print(A)
print(B)
print(C)

D = []
for i in A:
    D.append(i)
for i in B:
    D.append(i)
for i in C:
    D.append(i)


print(D)

for i in range(len(D)-1):
    for j in range(len(D)-1-i):
        if D[j] <= D[j+1]:
            D[j], D[j+1] = D[j+1], D[j]



print(D)

    