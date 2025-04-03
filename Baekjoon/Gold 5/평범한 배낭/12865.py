"""
https://www.acmicpc.net/problem/12865

[ Dynamic Programming ]

https://velog.io/@min_gi1123/c-%EB%B0%B1%EC%A4%80-12865-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%AD-%EB%B0%B0%EB%82%AD-%EB%AC%B8%EC%A0%9C-Knapsack-Problem

dp[i][j] : 최대 용량이 j일 때, i번째까지 item을 봤을 때 최대의 가치 ··· (1)

i 번째 item을 볼 때 그 무게(weight)가 j 보다 작다면
이 물건은 가방에 담을 수 있는 상태이다 ··· (2)

이 때 이 물건을 담는 것과 담지 않는 것 중 큰 가치를 택한다 ··· (3)

담을 수 없다면 ··· (4)

최대 용량이 동일할 때, i-1 번째 item까지 본 것을 택한다 ··· (5)
"""

import sys

N, K = map(int, sys.stdin.readline().split())
weight_value = [[0, 0]]
# (1)
dp = [[0 for j in range(K + 1)] for i in range(N + 1)]

for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    weight_value.append([w, v])

for i in range(1, N + 1):
    weight = weight_value[i][0]
    value = weight_value[i][1]

    for j in range(1, K + 1):
        # (2)
        if j >= weight:
            # (3)
            dp[i][j] = max(dp[i-1][j - weight] + value, dp[i - 1][j])
        # (4)
        else:
            # (5)
            dp[i][j] = dp[i-1][j]

# sys.stdout.write(f"{dp}\n") - for debug
sys.stdout.write(f'{dp[N][K]}')
