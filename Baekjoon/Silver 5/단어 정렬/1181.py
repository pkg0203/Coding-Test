"""
https://www.acmicpc.net/problem/1181
[ Sorting ]

중복을 없애기 위해 set으로 dictionary를 선언 ··· (1)

개행문자를 받지 않기 위해 마지막 글자를 제외하고 set에 추가 ··· (2)

list로 바꾼 후 정렬을 진행
이 때 첫번째 기준은 길이이고, 두번째 기준은 자기자신 
즉 사전순(str이기 때문)이 된다 ··· (3)
"""

import sys

N = int(sys.stdin.readline())
# (1)
dictionary = set()
# (2)
for _ in range(N):
    dictionary.add(sys.stdin.readline()[:-1])
# (3)
answer = sorted(list(dictionary),key = lambda x: (len(x),x))

for word in answer :
    sys.stdout.write(f"{word}\n")
