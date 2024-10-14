"""
https://www.acmicpc.net/problem/14425
[ HashMap ]
N에 속하는 String을 Dictionary에 저장하고
M에 속하는 String은 Dictionary에서 확인
"""

import sys

N,M = map(int,sys.stdin.readline().split())
STR_DICT = {}
for i in range(N):
    STR_DICT[sys.stdin.readline()] = 0

answer = 0
for i in range(M):
    if sys.stdin.readline() in STR_DICT.keys():
        answer +=1
sys.stdout.write(f"{answer}")