S = input()
stringA = ''
x = 0
if S.count(" ") >= 2:
    c1 = S.find(" ")
    c2 = S.find(" ", c1+1)
    print(S[c1+1:c2])

else: print(S)