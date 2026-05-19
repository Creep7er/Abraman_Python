C_1 = input("C_1 ")
C_2 = input("C_2 ")

N = int(input("N "))

stroka = ""
for i in range(N):
    if i % 2 == 0:
        stroka += str(C_1)
    elif i % 2 != 0:
        stroka += str(C_2)

print(stroka)