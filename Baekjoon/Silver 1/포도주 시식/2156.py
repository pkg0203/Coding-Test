"""
https://www.acmicpc.net/problem/2156
[ Dynamic Programming ]

dp[i] : i 번째 잔까지 마실 수 있는 최대의 양

dp[0] : 첫잔을 마신다
dp[1] : 첫잔과 두번째 잔을 마신다
dp[2] : 세 잔 중 가장 적은 양은 마시지 않는다
로 초기화 한다 ··· (1)

현재 잔을 마시는 경우는 아래와 같다
[][X][O][O] : 현재 잔 + 이전잔 + dp[i-3]
   [][X][O] : 현재 잔 + dp[i-2]
마시지 않는 경우는 아래와 같다
      [][X] : dp[i-1]
이 중 최대로 계속 채워나간다 ··· (2)
"""

import sys

N = int(sys.stdin.readline())
drinks = []

for _ in range(N):
    drinks.append(int(sys.stdin.readline()))

# (1)
dp = [ 0 for _ in range(N) ]
if N >=3 :
    dp[2] = sum(drinks[:3])-min(drinks[:3])
if N >= 2 :
    dp[1] = drinks[0] + drinks[1]
dp[0] = drinks[0]

# (2)
for i in range(3,N) :
    dp[i] = max(drinks[i]+drinks[i-1]+dp[i-3],drinks[i]+dp[i-2],dp[i-1])
sys.stdout.write(f"{dp[N-1]}")