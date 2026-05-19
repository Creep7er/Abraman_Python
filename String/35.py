S = input()
S_0 = input()
if S_0 in S:
    stringA = ""
    S_S = S.split(S_0)
    for i in range(len(S_S)):
        stringA += S_S[i]
    print(stringA)
    
else:
    print(S)