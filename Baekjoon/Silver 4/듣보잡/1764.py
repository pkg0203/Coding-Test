"""
https://www.acmicpc.net/problem/1764
[ HashMap ]

듣도 못한 사람만 HashMap에 저장 ··· (1)

보도 못한 사람이 HashMap에 있으면
answer에 저장한다 ··· (2)

answer를 사전 순으로 정렬하고 출력
"""

import sys

N,M = map(int,sys.stdin.readline().split())

hashmap = {}

# (1)
for _ in range(N):
    hashmap[sys.stdin.readline().strip()]=1

answer = []
# (2)
for _ in range(M):
    input = sys.stdin.readline().strip()
    if hashmap.get(input):
        answer.append(input)
answer.sort()
sys.stdout.write(f"{len(answer)}\n")
for name in answer:
    sys.stdout.write(f"{name}\n")
