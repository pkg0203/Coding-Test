"""
https://www.acmicpc.net/problem/2225
[ Mathematics ]
[ Dynamic Programming ]

"""
R = 1000000000

def initialize():
    for i in range(N+1):
        dp[i][1] = 1
    if K >=2 :
        for i in range(N+1):
            dp[i][2] = i+1
    if K >=3 :
        for i in range(N+1):
            dp[i][3] = (i+1)*(i+2)//2

import sys
N,K = map(int,sys.stdin.readline().split())

dp = [[0 for i in range(K+1)] for j in range(N+1)]
initialize()
if K < 4 :
    sys.stdout.write(f"{dp[N][K]}\n")

else :
    for i in range(N+1):
        for j in range(4,K+1):
            for k in range(i+1):
                dp[i][j] += dp[k][j-1]
            dp[i][j] %= R
    sys.stdout.write(f"{dp[N][K]}\n")