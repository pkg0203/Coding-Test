# https://www.acmicpc.net/problem/1316

import sys

T = int(sys.stdin.readline())
answer = 0
for testcase in range(T):
    checker = []
    switch = True
    word = sys.stdin.readline()[:-1]
    for char in word:
        # First appear
        if not char in checker:
            checker.append(char)
        # Had already appeared
        else:
            # Not Continuous
            if checker[-1] != char:
                switch = False
                break
    if switch:
        answer += 1
sys.stdout.write(str(answer))
