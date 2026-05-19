S = input("Вводи выражение: ")
SUM = int(S[0])
for i in range(1, len(S), 2):
    if S[i] == "+":
        SUM += int(S[i+1])
    elif S[i] == "-":
        SUM -= int(S[i+1])
    
print(SUM)