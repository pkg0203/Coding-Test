"""
https://www.acmicpc.net/problem/1629

[ Divide and Conquer ]

A power B를 Divide and Conquer로 구하는 알고리즘 ··· (1)

"""

import sys

A,B,C = map(int,sys.stdin.readline().split())
answer = 1
# (1)
while B:
    if B%2==1:
        B-=1
        answer *= A
    A*=A
    B//=2

    A%=C
    answer %= C

sys.stdout.write(f'{answer}')
