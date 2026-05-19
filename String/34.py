S = input()
S_0 = input()
if S_0 in S:
    print(S.rsplit(S_0, 1)[0])
else:
    print(S)