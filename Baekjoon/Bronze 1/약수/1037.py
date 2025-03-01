"""
https://www.acmicpc.net/problem/1037

[ Mathematics ]
"""

import sys

N = int(sys.stdin.readline())
factors = list(map(int,sys.stdin.readline().split()))
answer = 0

if len(factors) == 1:
    answer = factors[0]**2
else:
    answer = min(factors) * max(factors)
sys.stdout.write(f"{answer}")