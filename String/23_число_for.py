S = input("Вводи выражение: ")
i  = 0
flag = 0
SUM = 0
K = ""
for i in range(len(S)):
    if S[i] == "+":
        if flag == 0:
            SUM += int(K)
            K = ""
        elif flag == 1:
            SUM -= int(K)
            K = ""
        flag = 0
    elif S[i] == "-":
        if flag == 0:
            SUM += int(K)
            K = ""
        elif flag == 1:
            SUM -= int(K)
            K = ""
        flag = 1
    else:
        K += S[i]
        if i == len(S) - 1:
            if flag == 0:
                SUM += int(K)
                K = ""
            elif flag == 1:
                SUM -= int(K)
                K = ""
            
print(SUM)