S = input("Непустую строку введи: ")
counter = 0
alpha_low = []
for i in range(97, 122):
    alpha_low.append(chr(i))
    
def thing(x):
    return x.upper()

mapped_string = "".join(map(thing, S))

print(mapped_string)