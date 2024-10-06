"""
https://www.acmicpc.net/problem/25305
[ Sorting ]

내림차순으로 정렬한 후 ··· (1)

K번째 원소를 출력하면 된다 ··· (2)
"""

import sys

N, K = map(int,sys.stdin.readline().split())
# (1)
scores = sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
# (2)
sys.stdout.write(f"{scores[K-1]}\n")
