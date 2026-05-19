S = input("Непустую строку введи: ")
numbers = 0

for i in S:
    if i.isdigit():
        numbers += 1

print(numbers)