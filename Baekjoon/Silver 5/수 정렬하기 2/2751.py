"""
https://www.acmicpc.net/problem/2751
[ Sorting ]

오름차순 정렬 후 프린트하면 된다
"""

import sys

N = int(sys.stdin.readline())
answer = []
for i in range(N):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in range(N):
    sys.stdout.write(f"{answer[i]}\n")