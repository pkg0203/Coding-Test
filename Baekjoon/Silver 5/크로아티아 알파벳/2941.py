# https://www.acmicpc.net/problem/2941

import sys

CROATIA_ALPHABET_2 = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
CROATIA_ALPHABET_3 = "dz="

word = sys.stdin.readline()[:-1]
walker = 0
answer = 0
# Out Of Index 처리하기 싫어서 try-except로 구현
while walker < len(word):
    try:
        three = word[walker : walker + 3]
        if three == CROATIA_ALPHABET_3:
            answer += 1
            walker += 3
            continue
    except:
        pass

    try:
        two = word[walker : walker + 2]
        if two in CROATIA_ALPHABET_2:
            answer += 1
            walker += 2
            continue
    except:
        pass
    answer += 1
    walker += 1
sys.stdout.write(str(answer))
