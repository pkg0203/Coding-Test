"""
https://www.acmicpc.net/problem/1654

[ Binary Search ]
"""

import sys

N, K = map(int, sys.stdin.readline().split())
lines = []
l = 1
r = 0

for _ in range(N):
    line = int(sys.stdin.readline())
    r = max(r,line)
    lines.append(line)




while l<=r:
    mid = (l + r) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid
    if cnt < K:
        r = mid - 1

    elif cnt >= K:
        l = mid + 1

sys.stdout.write(f"{r}")