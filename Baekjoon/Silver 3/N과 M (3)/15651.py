"""
https://www.acmicpc.net/problem/15651

[ Back Tracking ]
"""


def print_permutation(N, M):
    global arr
    if len(arr) == M:
        sys.stdout.write(f"{' '.join(arr)}\n")
        return
    for i in range(1, N + 1):
        arr.append(str(i))
        print_permutation(N, M)
        arr.pop()


import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
print_permutation(N, M)
