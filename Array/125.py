import random

# ------- Заполнение массива
N = 20  # int(input('N '))
A = []

for _ in range(N):
    A.append(random.randint(1, 9))
#A = [1, 1, 3, 3, 2, 4, 1, 4, 4, 5]
A.sort()
print(A)
# ------- Заполнение массива

K = int(input('K? ')) 
lena = 1
index2 = len2 = None
x = N-1
while x > 0:

    if A[x] != A[x-1]:
        if lena < K:
            index_k = x
            len_k = lena
            print(index_k, len_k)
            for i in range(len_k):
                print("Pop", A.pop(index_k))
            A.insert(index_k, 0)
            
        lena = 1
    else:
        lena += 1
    x -= 1
    print(x)
print(index_k, len_k)
print(A)