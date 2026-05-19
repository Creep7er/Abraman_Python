S = input("Вводи выражение: ")
SUM = 0
LS = S

while True:
    plus_cord = LS.find("+")
    minus_cord = LS.find("-")

    if plus_cord == -1 and minus_cord == -1:
        SUM += int(LS)
        break

    if plus_cord == -1:
        op_cord = minus_cord
        op = "-"
    elif minus_cord == -1:
        op_cord = plus_cord
        op = "+"
    else:
        if plus_cord < minus_cord:
            op_cord = plus_cord
            op = "+"
        else:
            op_cord = minus_cord
            op = "-"

    left = LS[:op_cord]
    right = LS[op_cord + 1:]

    if op == "+":
        SUM += int(left)
    else:
        SUM -= int(left)

    LS = right

print(SUM)