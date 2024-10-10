"""
https://www.acmicpc.net/problem/1932
[ Dynamic Programming ]

dp[i][j] : 삼각형 (i,j) 까지의 합의 최댓값 ··· (1)

dp[0][0]는 순회에 포함할 필요가 없음 ··· (2)

level i에는 i까지의 index까지 있기 때문 ··· (3)

j가 맨 왼쪽이면 오른쪽 상단의 값을 그냥 더한다 ··· (4)

j가 맨 오른쪽이면 왼쪽 상단의 값을 그냥 더한다 ··· (5)

j가 양 끝이 아니면 왼쪽 상단과 오른쪽 상단 중 큰 값을 더한다 ··· (6)

결과적으로 dp의 맨 아래에는 해당 원소로 끝나는 합 중 가장 큰 값이 적혀있는데
이 중 최대가 답이 된다 ··· (7)
"""

import sys

N = int(sys.stdin.readline())

dp = []

# (1)
for _ in range(N):
    dp.append(list(map(int,sys.stdin.readline().split())))

# (2)
for i in range(1,N):
    # (3)
    for j in range(i+1):
        # (4)
        if j == 0 :
            dp[i][j] += dp[i-1][j]
        # (5)
        elif j == i :
            dp[i][j] += dp[i-1][j-1]
        # (6)
        else :
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])
# (7)
sys.stdout.write(f"{max(dp[N-1])}")