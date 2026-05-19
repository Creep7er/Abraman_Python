import random
# ------- Заполнение массива
N = int(input(''))
lst = []

for _ in range(N):
    lst.append(random.randint(1, 10))

# ------- Заполнение массива
print(lst)
ANS = []
S = 0

def summator_3000(i):
    S = 0
    for x in range(i, len(lst)):
        S += lst[x]
    return S
for i in range(len(lst)):
    S += lst[i]
    ANS.append(summator_3000(i))


print(ANS)

    