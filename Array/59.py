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
for i in range(len(lst)):
    S += lst[i]
    ANS.append(S/(i+1))


print(ANS)

    