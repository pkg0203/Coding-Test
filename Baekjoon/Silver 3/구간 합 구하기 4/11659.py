"""
https://www.acmicpc.net/problem/11659

[ Prefix Sum ]

sums[i] : i번째 원소까지의 합

i번째부터 j번째 원소의 합 = sums[j] - sums[i]
"""

import sys

N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
sums = [0] + [0 for i in range(N)]

for i in range(1,N+1):
    sums[i] = sums[i-1] + nums[i-1]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    sys.stdout.write(f"{sums[b]-sums[a-1]}\n")