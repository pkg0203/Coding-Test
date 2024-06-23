# https://www.acmicpc.net/problem/9461

import sys

CONSTANT = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
T = int(sys.stdin.readline())
for testcase in range(T):
    N = int(sys.stdin.readline())
    while True:
        # Whether answer is exist
        try:
            sys.stdout.write(f"{CONSTANT[N]}\n")
            break
        # If not, calculate next term
        except:
            CONSTANT.append(CONSTANT[-1] + CONSTANT[-5])
