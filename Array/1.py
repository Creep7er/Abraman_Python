N = int(input())

lst = [1]

for i in range(N):
    lst.append(lst[i] + 2)

print(lst)
