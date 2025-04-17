"""
https://www.acmicpc.net/problem/13305

[ Greedy Algorithm ]

도시를 나아가면서 이전에 나왔던 기름보다 싸면
이 기름으로 채워간다

그렇지 않으면 이전 기름으로 치운다
"""

import sys
import math

N = int(sys.stdin.readline())
distances = list(map(int,sys.stdin.readline().split()))
prices = list(map(int,sys.stdin.readline().split()))

min_price = math.inf
answer = 0

for i in range(N-1):
    price = prices[i]
    if price < min_price:
        min_price = price
    answer += min_price * distances[i]

sys.stdout.write(f"{answer}")