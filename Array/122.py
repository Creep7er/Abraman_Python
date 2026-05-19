import random

# ------- Заполнение массива
N = 10  # int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 5))
#A = [1, 1, 1, 3, 2, 4, 1, 4, 4, 5]
print(A)
# ------- Заполнение массива

K = int(input('K? '))

seria_num = 0 
i = 0

while i < len(A):
    seria_num += 1
    seria_start = i
    value = A[i]
    
    while i + 1 < len(A) and A[i + 1] == value: #конец серии
        i += 1
    
    seria_end = i
    seria_length = seria_end - seria_start + 1
    
    if seria_num == K:
        for j in range(seria_length):
            A.pop(seria_start)
        break
    
    i += 1

print(A)