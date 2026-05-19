S = input()
stringA = ''
x = 0
if S.count(" ") >= 2:
    c1, c2 = S.find(" "), S.rfind(" ")
    print(S[c1+1:c2])

else: print(S)