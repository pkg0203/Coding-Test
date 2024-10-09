"""
https://www.acmicpc.net/problem/10814
[ Stable Sort ]

정렬 시 기준을 나이로만 설정하면, 가입 순 정렬은 구현하지 않아도 된다
"""

import sys

N = int(sys.stdin.readline())
accounts = []

for _ in range(N):
    age,name = sys.stdin.readline().split()
    accounts.append([int(age),name])
accounts.sort(key=lambda x:x[0])

for account in accounts:
    sys.stdout.write(f"{account[0]} {account[1]}\n")