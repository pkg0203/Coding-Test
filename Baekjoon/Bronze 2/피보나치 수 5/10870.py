"""
https://www.acmicpc.net/problem/10870

[ Recursion ]

"""

import sys

def fibo(N):
    if N == 1:
        return 1
    elif N == 0:
        return 0
    return fibo(N-1) + fibo(N-2)

N = int(sys.stdin.readline())
answer = fibo(N)
sys.stdout.write(f"{answer}")