S = input("Непустую строку введи: ")
if S.count(".") == 1:
    if S.replace(".", "").isdigit():
        ans = 2
    else:
        ans = 0
elif S.isdigit():
    ans = 1
else: ans = 0

print(ans)