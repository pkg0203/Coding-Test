"""
https://www.acmicpc.net/problem/2839

[ Dynamic Programming ]

DP 에 값이 있으면 출력 ··· (1)
단, 만들 수 없는 경우(infinity)는 -1로 출력 ··· (2)

DP 에 없으면 3 또는 5를 뺀 것에서 최소인 것을 택함 ··· (3)

"""
import sys
import math

inf = math.inf
dp = [0, inf, inf, 1, inf, 1]

N = int(sys.stdin.readline())
while True:
    try:
        # (2)
        if dp[N]==inf:
            sys.stdout.write(f"-1")
        # (1)
        else:
            sys.stdout.write(f"{dp[N]}")
        break
    # (3) 
    except:
        dp.append(min(dp[-3], dp[-5]) + 1)
