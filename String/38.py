S = input()
S_1 = input()
S_2 = input()
stringA = ''
x = 0
if S_1 in S:
    S_S = S.split(S_1)
    while x < len(S_S):
        if S_S[x] == "":
            S_S.insert(x, S_2)
            x +=1
        x+=1
    for i in range(len(S_S)):
        stringA += S_S[i]
    print(stringA)
else: print(S)