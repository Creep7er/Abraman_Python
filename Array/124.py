import random

# ------- Заполнение массива
N = 20  # int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(5, 9))
#A = [1, 1, 3, 3, 2, 4, 1, 4, 4, 5]
A.sort()
print(A)
# ------- Заполнение массива

K = int(input('K? ')) 
s = 1
lena = 1
index2 = len2 = None
sernepal = 1


seri = 0

for x in range(1,N):
    if A[x] != A[x-1]:
        seri += 1

for i in range(N-1, 0, -1):

    if A[i] != A[i-1]:
        sernepal += 1
        if sernepal == 2:
            index_l = -1
            len_l = lena
        lena = 1
    else:
        lena += 1

for x in range(1,N):

    if A[x] != A[x-1]:
        s += 1
        if s == K+1:
            index2 = x - lena 
            len2 = lena
        lena = 1
    elif i == 1 and s == K == 1:
        index2 = 0
        len2 = lena + 1
    else:
        lena += 1

print(index_l, len_l, index2, len2)
if index2 is None or len2 is None:
    print(A)
else:
    a = A[0:index2]
    b = A[index2:index2+len2]
    c = A[index2+len2:index_l-len_l]
    d = A[index_l-len_l+1:]
    if K == 1:
        A = d + c + b + a
    else: A = a + d + c + b
    print(a, b, c, d)
    print(A)
