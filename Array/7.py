lst = []
i = 0
while True:
    i += 1
    N = int(input())
    if N == 0:
        break
    else:
        lst.append(i)

print(lst[::-1])