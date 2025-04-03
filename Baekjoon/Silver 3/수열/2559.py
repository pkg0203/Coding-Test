"""
https://www.acmicpc.net/problem/2559

[ Prefix Sum ]

sums[i] : nums[i]까지의 합, 즉 sum(nums[:i+1])과 같음 ··· (1)

이제 이를 이용하여 
시작점이 0부터 N-K-1번째까지 K개의 원소를 더해서
p_sum을 계산하여 최대값을 찾는다 ··· (2)

"""

import sys
import math

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# (1)
sums = [0]
for i in range(1, N+1):
    sums.append(sums[i-1] + nums[i-1])

answer = -math.inf

# (2)
for i in range(N - K + 1):
    p_sum = sums[i + K] - sums[i]
    if answer < p_sum:
        answer = p_sum
sys.stdout.write(f"{answer}")
