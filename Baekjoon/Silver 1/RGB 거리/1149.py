"""
https://www.acmicpc.net/problem/1149
[ Dynamic Programming ]

DP[i][j] : i번째 집에 j번째 색을 칠했을 때 최소의 비용 ··· (1)

i번째 빨간색이면 i-1번째 집이 초록색이나 파란색까지의 최소비용 중 최소를 더한다 ··· (2)

i번째 초록색이면 i-1번째 집이 빨간색이나 파란색까지의 최소비용 중 최소를 더한다 ··· (3)

i번째 파란색이면 i-1번째 집이 초록색이나 빨간색까지의 최소비용 중 최소를 더한다 ··· (4)

마지막 집을 빨,초,파로 칠했을 때 각각의 최소비용이 있을 것이고, 그 중 최소가 답이다 ··· (5)
"""

import sys

N = int(sys.stdin.readline())
# (1)
DP_RGB_COST = []

for _ in range(N):
    DP_RGB_COST.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,N) :
    for j in range(3):
        # (2)
        if j == 0:
            DP_RGB_COST[i][0] += min(DP_RGB_COST[i-1][1],DP_RGB_COST[i-1][2])
        # (3)
        if j == 1:
            DP_RGB_COST[i][1] += min(DP_RGB_COST[i-1][0],DP_RGB_COST[i-1][2])
        # (4)
        if j == 2:
            DP_RGB_COST[i][2] += min(DP_RGB_COST[i-1][1],DP_RGB_COST[i-1][0])
# (5)
sys.stdout.write(f"{min(DP_RGB_COST[N-1])}")