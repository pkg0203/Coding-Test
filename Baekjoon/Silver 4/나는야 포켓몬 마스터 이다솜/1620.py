"""
https://www.acmicpc.net/problem/1620
[ HashMap ]

N 만큼 포켓몬을 도감에 등록 ··· (1)

M만큼 order를 입력받는다
이 때 order가 int라면 포켓몬을 출력 ··· (2)

order가 str이라면 index (도감번호)를 출력 ··· (3)
"""

import sys

N, M = map(int, sys.stdin.readline().split())

poketmon = {}
# (1)
for number in range(1,N+1):
    po=sys.stdin.readline()[:-1]
    poketmon[po] = number
    poketmon[number] = po

for _ in range(M):
    order = sys.stdin.readline()[:-1]
    # (2)
    try:
        order = int(order)
        sys.stdout.write(f"{poketmon[order]}\n")
    # (3)
    except:
        sys.stdout.write(f"{poketmon[order]}\n")