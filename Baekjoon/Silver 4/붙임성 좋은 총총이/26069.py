"""
https://www.acmicpc.net/problem/26069

"""

import sys

rainbow_dance = {'ChongChong':1}

N = int(sys.stdin.readline())

for _ in range(N) :
    a,b = map(str,sys.stdin.readline()[:-1].split())
    if rainbow_dance.get(a) or rainbow_dance.get(b):
        rainbow_dance[a] = 1
        rainbow_dance[b] = 1

answer = len(list(rainbow_dance.keys()))
sys.stdout.write(f"{answer}")