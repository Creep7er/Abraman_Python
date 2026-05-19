S = input("Непустую строку введи: ")
counter = 0
alpha_low = []
for i in range(65, 91):
    alpha_low.append(chr(i))
for i in S:
    if i in alpha_low:
        counter += 1

print(counter)