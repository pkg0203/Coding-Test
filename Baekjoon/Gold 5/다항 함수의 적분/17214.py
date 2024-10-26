"""
[ Mathematics ]

2x+1
2x-1
-2x+1
-2x-1
"""


def antiderivative():
    coef[1] //= 2


def print_coef(num, is_first):
    if is_first:
        if num == -1:
            return "-"
        if num == 1:
            return ""
        else:
            return num
    else:
        if num == -1:
            return "-"
        if num == 1:
            return "+"
        if num > 0:
            return "+" + str(num)
        else:
            return num


import sys

func = sys.stdin.readline().strip()
coef = [None, None]


if not "x" in func:
    coef[1] = 0
    coef[0] = int(func)
elif func.split('x')[1] =="":
    coef[1] = int(func.split("x")[0])
    coef[0] = 0
else:
    coef[1] = int(func.split("x")[0])
    coef[0] = int(func.split("x")[1])
antiderivative()

if coef[1] == 0 and coef[0] == 0:
    sys.stdout.write("W")
elif coef[1] == 0:
    sys.stdout.write(f"{print_coef(coef[0],True)}x+W")
elif coef[0] == 0:
    sys.stdout.write(f"{print_coef(coef[1],True)}xx+W")
else:
    sys.stdout.write(f"{print_coef(coef[1],True)}xx{print_coef(coef[0],False)}x+W")