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
for x in range(1,N):

    if A[x] != A[x-1]:
        s += 1
        if s == 2:
            index1 = 0
            len1 = lena
        if s == K+1:
            index2 = x - lena 
            len2 = lena
        lena = 1
    elif x == N-1 and s == K:
        index2 = N-1-lena
        len2 = lena + 1
    else:
        lena += 1

print(index1, len1, index2, len2)
if index2 is None or len2 is None:
    print(A)
else:
    a = A[0:len1]
    b = A[len1:index2]
    c = A[index2:index2 + len2]
    d = A[index2+len2:]
    A = c + b + a + d
    print(A)
