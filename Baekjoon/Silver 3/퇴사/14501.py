"""
https://www.acmicpc.net/problem/14501
[ Dynamic Programming ]

dp[i] : i번째 상담을 받을 때, 0부터 i번째까지의 최대 이익

k 일에 상담이 만약 (N-K)일이 소요된다면 이 상담은 어차피 받을 수 없으므로
dp[k]를 0으로 초기화한다 ··· (1)

dp[i] 가 0이라면 계산할 필요없으므로 넘긴다 ··· (2)

i번째 상담을 받을 때, j번째를 받을 수 있다면 ··· (3)

j번째를 받을지 말지 max를 통해 결정한다
j+1에서 max가 될 수도 있기 때문이다 ··· (4)
"""

import sys


N = int(sys.stdin.readline())

time =[]
pay = []

for _ in range(N):
    data=list(map(int,sys.stdin.readline().split()))
    time.append(data[0])
    pay.append(data[1])

dp = [pay[i] for i in range(N)]

#(1)
for i in range(N):
    if i+time[i]>N:
        dp[i]=0

for i in range(1,N):
    # (2)
    if dp[i] == 0:
        continue
    for j in range(i):
        # (3)
        if j+ time[j] <= i:
            # (4)
            dp[i] = max(dp[j]+pay[i],dp[i])
sys.stdout.write(f"{max(dp)}")