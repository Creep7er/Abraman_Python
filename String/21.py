S = input("Введите целое длинное положительное число: ")

def fufufufunc(x):
    return str(ord(x))

mapped_string = "".join(map(fufufufunc, S[::-1]))

print(mapped_string)