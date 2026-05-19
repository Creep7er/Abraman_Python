from math import inf
S = input()

S_S = S.split(" ")
print(S_S)
x = 0
stringA = ''
while x < len(S_S)-1:
    if S_S[x] != "":
        S_S[x] += "."
    x+=1
for i in range(len(S_S)):
    stringA += S_S[i]
print(stringA)