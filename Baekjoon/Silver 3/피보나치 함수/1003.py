"""
https://www.acmicpc.net/problem/1003
[ Dynamic Programming]

dp[N][0] : N에서 fibonacci(0)가 호출되는 횟수
dp[N][1] : N에서 fibonacci(1)가 호출되는 횟수
"""
import sys

dp = [
    [1,0],
    [0,1],
    [1,1],
    [1,2],
]

T = int(sys.stdin.readline())

for testcase in range(T):
    N = int(sys.stdin.readline())
    while True:
        try :
            sys.stdout.write(f"{dp[N][0]} {dp[N][1]}\n")
            break
        except:
            dp.append([dp[-1][0]+dp[-2][0],dp[-1][1]+dp[-2][1]])
