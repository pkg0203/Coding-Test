"""
https://www.acmicpc.net/problem/1463
[ Dynamic Programming ]

Bottom-up 방식으로
value에 해당하는 최소 연산수를 구한다

value가 3의 배수라면 3으로 나눈 a의 연산수를 확인한다 ··· (1)

value가 2의 배수라면 2로 나눈 b의 연산수를 확인한다 ··· (2)

1뺀 값의 연산수를 확인하고 이 중 최소가 value의 최소 연산수이다 
만약 a나 b가 0인 경우엔 infinity이므로 비교대상에서 빠진다 ··· (3)
"""
import sys
import math

dp = [math.inf, 0]

N = int(sys.stdin.readline())

while len(dp) < N + 1 :
    value = len(dp)
    a,b = 0 , 0
    # (1)
    if value % 3 == 0 :
        a = value // 3
    # (2)
    if value % 2 == 0 :
        b = value // 2
    # (3)
    dp.append( min ( dp[a] + 1 , dp[b] + 1 , dp[value-1] + 1))

sys.stdout.write(f"{dp[-1]}")