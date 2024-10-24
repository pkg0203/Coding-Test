"""
https://www.acmicpc.net/problem/32384
[ Implement ]
"""

import sys

SENTENCE = "LoveisKoreaUniversity"

N = int(sys.stdin.readline())
answer_list = []
for _ in range(N):
    answer_list.append(SENTENCE)
sys.stdout.write(f"{' '.join(answer_list)}")