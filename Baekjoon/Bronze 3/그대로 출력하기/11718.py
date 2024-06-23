# https://www.acmicpc.net/problem/11718

import sys

while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            break
        print(line)
    except EOFError:
        break
