# https://www.acmicpc.net/problem/1002

import sys


def dist_square(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


T = int(sys.stdin.readline())
for testcase in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = dist_square(x1, y1, x2, y2)
    sum_square = (r1 + r2) ** 2
    sub_square = (r1 - r2) ** 2
    # Same Center
    if d == 0:
        # Same Radius
        if sub_square == 0:
            result = -1
        # Different Radius
        else:
            result = 0
    # Different Center
    else:
        if d > sum_square:
            result = 0
        elif d == sum_square:
            result = 1
        elif d == sub_square:
            result = 1
        elif d < sub_square:
            result = 0
        elif d < sum_square:
            result = 2

    sys.stdout.write(f"{result}\n")
