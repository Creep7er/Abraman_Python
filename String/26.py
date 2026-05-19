S = input()
N = int(input())

if len(S) < N:
    while len(S) < N:
        S += "."
else:
    
    S = S[N:]

print(S)