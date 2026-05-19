stringA = input("Дай строку: ")

def thing(x):
    return x + " "

mapped_string = "".join(map(thing, stringA))

print(mapped_string)
