"""#Фибоначчи
N = int(input())



for i in range(2, N+1):
    a0 = a1 +a2
    a2 = a1
    a1 = a0
    print(a0)


"""

lst = []

N = int(input('N: '))
a1 = 0
a2 = 1
lst.append(a1)

for i in range(2, N+1):
    a0 = a1 +a2
    a2 = a1
    a1 = a0
    lst.append(a0)

print(lst)


