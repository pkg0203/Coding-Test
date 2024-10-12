"""
https://www.acmicpc.net/problem/1904
[ Dynamic Programming ]

dp[i] : 01타일로 만들 수 있는 i 자리 수
dp[0] = 0 이 맞지만 계산을 위해 1로 초기화
i번째 자리 수 = (i-1) 번째 수에 1을 붙임 + (i-2) 번째 수에 00을 붙임

그런데 위와 같은 방식으로 구현하면 Memory Out이므로
dp[i-2] = a
dp[i-1] = b 로 구현
dp[i] = dp[i-1] + dp[i-2] = b + a
dp[i-1] = dp[i] - dp[i-2] = b - a ··· (1)
"""

import sys

N = int(sys.stdin.readline())


a,b =1,1
# (1)
for i in range(2,N+1):
    a,b= b%15746,(b+a) % 15746
    
sys.stdout.write(f"{b}")