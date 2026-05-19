import random

# ------- Заполнение массива
N = 10  # int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 5))
A = [1, 1, 3, 3, 2, 4, 1, 4, 4, 5]
print(A)
# ------- Заполнение массива

K = int(input('K? ')) 

seria_num = 0 
i = 0

while i < len(A):
    if K == 1:
        break
    seria_num += 1
    seria_start = i
    seria_end = i
    value = A[i]

    while seria_end + 1 < len(A) and A[seria_end + 1] == value: #конец серии
        seria_end += 1
    seria_length = seria_end - seria_start + 1

    if seria_num == 1:
        first_seria_l = seria_length
        first_seria_v = value
        for _ in range(first_seria_l):
            A.pop(seria_start)
        #i -=  first_seria_l
    if seria_num == K:
        for y in range(seria_length-1):
            A.pop(seria_start)
            A.insert(0, value)
        for x in range(first_seria_l):
            A.insert(seria_end+i, first_seria_v)
            
#    print(i, A)
    
    i += 1
print(A)