"""
https://www.acmicpc.net/problem/11053
[ Dynamic Programming ]

dp[i] : i번째 원소로 마치는 LIS ( Longest Increasing Sequence ) 의 원소로 정의 ··· (1)

각각을 자신을 포함하므로 1로 초기화 ··· (2)

dp[0] 는 당연히 1이므로 i는 1부터 시작 ··· (3)

j는 i보다 왼쪽에 있게 되며 증가하는 수열인지 확인 ··· (4)

증가하는 수열의 경우 포함하거나 -> dp[j] + 1 
포함하지 않았을 때 -> dp[i] 
중에서 가장 큰 값을 취하도록 함 ··· (5)
"""

import sys

N = int(sys.stdin.readline())
# (1)
elements = list(map(int,sys.stdin.readline().split()))
# (2)
dp = [ 1 for _ in range(N) ]

# (3)
for i in range(1, N):
    for j in range(i):
        # (4)
        if elements[j] < elements[i]:
            # (5)
            dp[i] = max(dp[i], dp[j] + 1)

sys.stdout.write(f"{max(dp)}")
