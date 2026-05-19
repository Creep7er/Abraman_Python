S = input()
S_1 = input()
S_2 = input()
stringA = ''
if S_1 in S:
    S_S = S.rsplit(S_1, 1)
    cord = S_S.index("")
    S_S.insert(cord, S_2)
    for i in range(len(S_S)):
        stringA += S_S[i]
    print(stringA)
else: print(S)