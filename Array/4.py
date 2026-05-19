lst = []

N = int(input('N: '))
A = int(input('N[0]: '))
D = int(input('D: '))
lst.append(A)


for i in range(1, N+1):
    lst.append(A * i*D)
    print(f"{A}*{i}*{D}")

print(lst)
