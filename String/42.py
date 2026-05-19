S = input()

S_S = S.split(" ")
print(S_S)
counter = 0
for i in range(len(S_S)):
    if S_S[i] != "":
        word = str(S_S[i]) 
        if word[0] == word[-1]:
            counter += 1

print(counter)