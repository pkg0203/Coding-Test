"""
https://www.acmicpc.net/problem/11047

[ Greedy Algorithm ]

큰 동전부터 집는다.
"""

import sys

N,K = map(int,sys.stdin.readline().split())
coins = []
hand = 0
tot_count = 0

for times in range(N):
    coin = int(sys.stdin.readline())
    coins.append(coin)


for i in range(N-1,-1,-1):
    if coins[i] <= K - hand :
        count = ( K - hand ) // coins[i]
        hand += coins[i] * count
        tot_count += count
sys.stdout.write(f"{tot_count}")
