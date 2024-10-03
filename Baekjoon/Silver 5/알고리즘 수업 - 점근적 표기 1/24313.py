"""
https://www.acmicpc.net/problem/24313

[ Time Complexity ]

c가 a1보다 커야 하며, n0 이상의 n에 대해 조건이 만족해야 함 ··· (1)

이를 만족하지 못 하면 답이 아니다 ··· (2)
"""

import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

# (1)
if (a1 <= c) and ((c * n0) >= (a1 * n0 + a0)):
    sys.stdout.write("1")
# (2)
else:
    sys.stdout.write("0")
