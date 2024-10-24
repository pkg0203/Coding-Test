"""
https://www.acmicpc.net/problem/10844
[ Dynamic Programming ]

dp[i][j] : i 자리 수 중 j로 끝나는 계단수의 개수 ··· (1)

i번째가 0으로 끝나려면 i-1번째는 1로 끝나야 한다 ··· (2)

i번째가 9로 끝나려면 i-1번째는 8로 끝나야 한다 ··· (3)

i번째가 그 외의 수(1~8)로 끝나는 건 이웃한 두 수의 합이다 ··· (4)

정답을 10억으로 나눈 나머지를 출력하라 했으므로, 미리미리 나눠준다 ··· (5)

i 자리 계단수의 개수는 0부터 9까지 끝나는 수의 합이다 ··· (6)
"""

import sys

R = 1000000000

N = int(sys.stdin.readline())
# (1)
dp = [[0]+[1 for i in range(9)] for j in range(N+1)]

for i in range(2,N+1):
    for j in range(10):
        # (2)
        if j == 0 :
            dp[i][0] = dp[i-1][1]
        # (3)
        elif j == 9 :
            dp[i][9] = dp[i-1][8]
        # (4)
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        # (5)
        dp[i][j]%=R
# (6)
sys.stdout.write(f"{sum(dp[N])%R}")