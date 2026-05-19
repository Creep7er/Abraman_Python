S = input()
S_0 = input()
C = input()
M = list(S)
i = 0
while i < len(M):
    if M[i] == C:
        M.insert(i, S_0)
        i += 1
    i+=1
S = ""
for x in M:
    S += x

print(S)