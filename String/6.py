C = input("Дайте символ ")

C_CODE = ord(C)

if C_CODE in range(67, 91) or C_CODE in range(97, 123):
    print("lat")
elif C_CODE in range(1040, 1104):
    print("rus")