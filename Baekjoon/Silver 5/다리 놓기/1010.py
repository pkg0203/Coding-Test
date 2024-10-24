"""
https://www.acmicpc.net/problem/1010
[ Combinatorics ]

확률과 통계 많이 풀어봤다면, 역함수가 존재하는 경우의 수와 같은 문제다

즉 일대일 대응이 되도록 만들면 된다 ( 이 경우 증가함수 )

동쪽(M) 에서 서쪽(N) 을 뽑기만 하면 된다
"""

import sys
import math

T = int(sys.stdin.readline())

for testcase in range(T):
    N,M = map(int,sys.stdin.readline().split())
    print(math.comb(M,N))