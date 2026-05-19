import random
# ------- Заполнение массива
N = 10 #int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 5))

print(A)
# ------- Заполнение массива
#A = [1, 4, 5, 2, 2, 2, 4, 4, 3, 2]
B = []
C = []
count = 1
i = 0
while i < len(A)-1:

    if A[i] == A[i+1]:
        count += 1
    if A[i] != A[i+1]:
        A.insert(i-count+1, 0)
        i += 1
        count = 1
    if i == len(A)-2:
        if A[i] == A[len(A)-1]:
            A.insert(i-count+1, 0)
            i += 1
            count = 1
        else:
            A.insert(i+1, 0)
            i += 1
    i += 1

            
        

print(A)