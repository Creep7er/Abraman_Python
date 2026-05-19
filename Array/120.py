import random
# ------- Заполнение массива
N = 10 #int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 5))

print(A)
# ------- Заполнение массива
#A = [5, 5, 1, 5, 3, 3, 5, 2, 1, 1]
count = 1
i = 0
while i < len(A)-1:

    if A[i] == A[i+1]:
        count += 1
    if A[i] != A[i+1]:
        A.pop(i)
        i -= 1
    if i == len(A)-2:
        if A[i] == A[len(A)-1]:
            A.pop(i)
            i -= 1
            break
        if A[i] != A[len(A)-1]:
            A.pop(i+1)
            i -= 1
    i += 1
    print(A)

            
        

print(A)