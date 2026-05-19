S = input("Непустую строку введи: ")
counter = 0
alpha_low = []
for i in range(97, 122):
    alpha_low.append(chr(i))
    
for i in range(1072, 1103):
    alpha_low.append(chr(i))

for i in S:
    if i in alpha_low:
        counter += 1

print(counter)