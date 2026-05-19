import random

A = []
B = []
for _ in range(5):
    A.append(random.randint(1, 10))
for _ in range(5):
    B.append(random.randint(1, 10))

A.sort()
B.sort()
print(A)
print(B)


C = []
for i in A:
    C.append(i)
for i in B:
    C.append(i)


print(C)

for i in range(len(C)-1):
    for j in range(len(C)-1-i):
        if C[j] > C[j+1]:
            C[j], C[j+1] = C[j+1], C[j]



print(C)

    