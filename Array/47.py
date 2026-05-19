import random
# ------- Заполнение массива
N = int(input(''))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 10))

# ------- Заполнение массива
lst.sort()
print(lst)
ANS = []
count = 0
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            if lst[i] not in ANS:
                ANS.append(lst[i])

for i in ANS:
    if i in lst:
        count += 1

print(ANS)
print(len(lst) - count)
