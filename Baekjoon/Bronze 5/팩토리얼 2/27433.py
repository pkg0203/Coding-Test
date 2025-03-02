"""
https://www.acmicpc.net/problem/27433

[ Recursion ]
"""


def factorial(N):
    global answer
    if N > 0:
        return N * factorial(N - 1)
    else:
        return 1


import sys

N = int(sys.stdin.readline())
answer = factorial(N)
sys.stdout.write(f"{answer}")
