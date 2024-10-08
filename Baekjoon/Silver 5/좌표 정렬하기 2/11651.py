"""
https://www.acmicpc.net/problem/11651
[ Sorting ]

정렬 시, y좌표를 첫 번째 기준으로 x좌표를 두 번째 기준으로 정렬 ··· (1)
"""

import sys

N = int(sys.stdin.readline())
dots = []
for _ in range(N):
    dots.append(list(map(int,sys.stdin.readline().split())))
# (1)
dots.sort(key = lambda x:(x[1],x[0]))

for dot in dots:
    sys.stdout.write(f"{dot[0]} {dot[1]}\n")