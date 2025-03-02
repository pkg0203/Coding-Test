"""
https://www.acmicpc.net/problem/20920

"""

import sys

N,M = map(int,sys.stdin.readline().split())

eng_dict = {}
for _ in range(N):
    word = sys.stdin.readline()[:-1]
    if len(word) >= M:
        if eng_dict.get(word):
            eng_dict[word] += 1
        else:
            eng_dict[word] = 1

eng = sorted(list(eng_dict.items()),key = lambda x: (-x[1],-len(x[0]),x[0]))
for answer in eng:
    sys.stdout.write(f"{answer[0]}\n")