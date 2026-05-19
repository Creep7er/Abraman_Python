S = input("Непустую строку введи: ")
N = int(input("Нужно число: "))

def thing(x):
    return x + "*"*N 

mapped_string = "".join(map(thing, S))

print(mapped_string)