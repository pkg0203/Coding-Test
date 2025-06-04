"""
https://www.acmicpc.net/problem/11444

[ Divide and Conquer ]

도가뉴 항등식을 활용하기 위해 아래의 사이트 참고
https://jamie2779.tistory.com/56

짝수인 경우의 계산 ··· (1)

홀수인 경우의 계산 ··· (2)
"""

R = 1_000_000_007
import sys

sys.setrecursionlimit(10**8)
memo = {}
memo[0] = 0
memo[1] = 1
memo[2] = 1


def dp(i):
    if i not in memo:
        # (1)
        if i % 2 == 0:
            memo[i] = (dp(i // 2) * (dp(i // 2) + 2 * dp(i // 2 - 1))) % R
        # (2)
        else:
            memo[i] = (dp(i // 2) ** 2 + dp(i // 2 + 1) ** 2) % R
    return memo[i]


N = int(sys.stdin.readline())
answer = dp(N)
sys.stdout.write(f"{answer}")
