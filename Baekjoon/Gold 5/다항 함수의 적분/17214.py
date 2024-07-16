# https://www.acmicpc.net/problem/17214

import sys

polynomial = sys.stdin.readline()[:-1].split("+")
antiderivative = []
CONSTANT_OF_INTEGRATION = "W"
for coef in polynomial:
    if antiderivative:
        antiderivative.append(coef + "x")
    else:
        coef_num = coef.split("x")[0]
        antiderivative.append(f"{int(coef_num)//2}xx")
# filtering 1
for idx in range(2):
    term = antiderivative[idx]
    # eliminate x or xx
    if idx == 0:
        coef_num = term[:-2]
    else:
        coef_num = term[:-1]
    # update antiderivative for eliminate 1
    if coef_num == "1":
        antiderivative[idx] = term[1:]
antiderivative.append(CONSTANT_OF_INTEGRATION)
sys.stdout.write(f"{'+'.join(antiderivative)}")
