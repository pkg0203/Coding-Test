"""
https://www.acmicpc.net/problem/2579

[ Dynamic Programming ]

dp[i] : i번째 계단을 밟았을 때까지의 최댓값 -> 마지막 계단을 밟아야 하기 때문

dp[1]과 dp[2]는 손쉽게 초기화 할 수 있다 ··· (1)

i 번째 계단을 밟는 경우의 수는 아래와 같이 2가지 밖에 없다 ··· (2)
1 ) X O O = i-1번째를 밟고 i-2번째를 안 밟는 경우
          => 계단을 2개 건너 뛸 수는 없기 때문에 dp[i-3]이 필요
2 ) O X O = i-1번째를 안 밟고 i-2번째를 밟는 경우

"""

import sys

N = int(sys.stdin.readline())
stairs = [0]

for _ in range(N):
    stairs.append(int(sys.stdin.readline()))
dp = [0 for i in range(N+1)]

# (1)
dp[1] = stairs[1]

if N > 1 :
    dp[2] = stairs[2] + stairs[1]

# (2)
for i in range(3,N+1):
    dp[i] = max(stairs[i-1]+dp[i-3],dp[i-2]) + stairs[i]

sys.stdout.write(f"{dp[N]}")
