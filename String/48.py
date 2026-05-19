from math import inf
S = input()

S_S = S.split()
print(S_S)
x = 0
stringA = ''
while x < len(S_S):
    word = S_S[x]
    word = word[0] + word[1:].replace(word[0], ".")
    S_S[x] = word + " "
    x += 1
for i in range(len(S_S)):
    stringA += S_S[i]
print(stringA)