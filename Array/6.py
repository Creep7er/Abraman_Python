lst = []

N = int(input("N "))
A = int(input("A "))
B = int(input("B "))

lst.append(A)
lst.append(B)
S = A + B
lst.append(S)

for i in range(2, N+2):
    S += lst[i]
    lst.append(S)

print(lst)