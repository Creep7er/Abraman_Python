import random
# ------- Заполнение массива
N = 10 #int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 5))

print(A)
# ------- Заполнение массива
B = []
C = []
count = 1
for i in range(len(A)-1):

    if A[i] == A[i+1]:
        count += 1
    if A[i] != A[i+1]:
        B.append(A[i])
        C.append(count)
        count = 1
    if i == len(A)-2:
        if A[i] == A[len(A)-1]:
            B.append(A[len(A)-1])
            C.append(count)
            count = 1
        if A[i] != A[len(A)-1]:
            B.append(A[len(A)-1])
            C.append(count)
            count = 1
    

            
        

print(B)
print(C)