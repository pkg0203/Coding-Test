"""
https://www.acmicpc.net/problem/2346
[ Stack & Queue ]

"""

import sys
from collections import deque


N = int(sys.stdin.readline())

orders = list(map(int, sys.stdin.readline().split()))
answer = []
bal_left = N
deq = deque()

for i in range(1, N + 1):
    deq.append(i)


while bal_left:
    bal_left -= 1
    balloon = deq[0]
    deq[0] = 0
    rot_order = orders[balloon - 1]
    answer.append(balloon)
    while rot_order and bal_left:
        if rot_order > 0:
            deq.rotate(-1)
            if deq[0] != 0:
                rot_order -= 1
        elif rot_order < 0:
            deq.rotate(1)
            if deq[0] != 0:
                rot_order += 1

sys.stdout.write(f"{' '.join(list(map(str,answer)))}")
