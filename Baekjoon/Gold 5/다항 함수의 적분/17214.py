# https://www.acmicpc.net/problem/17214

import sys

polynomial = sys.stdin.readline()[:-1].split("+")
antiderivative = []
CONSTANT_OF_INTEGRATION = "W"

for term in polynomial:
    # Constant term
    if term[-1] != "x":
        antiderivative.append(term + "x")
    # First order term
    else:
        coef_num = term.split("x")[0]
        if coef_num == "":  # case when coef is "x"
            coef_num = "1"
        elif coef_num == "-":  # case when coef is "-x"
            coef_num = "-1"
        new_coef = int(coef_num) // 2
        antiderivative.append(f"{new_coef}xx")

# filtering 1
for idx in range(len(antiderivative)):
    term = antiderivative[idx]
    # Second order term
    if term[-2] == "x":
        coef_num = term[:-2]
    # First order term
    else:
        coef_num = term[:-1]
    # update antiderivative for eliminate 1
    if coef_num == "1":
        antiderivative[idx] = term[1:]
    elif coef_num == "-1":
        antiderivative[idx] = "-" + term[2:]

antiderivative.append(CONSTANT_OF_INTEGRATION)
sys.stdout.write(f"{'+'.join(antiderivative)}")
