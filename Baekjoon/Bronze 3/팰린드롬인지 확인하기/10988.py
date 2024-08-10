# https://www.acmicpc.net/problem/10988

import sys

word = sys.stdin.readline()[:-1]
if word == word[::-1]:
    sys.stdout.write("1")
else:
    sys.stdout.write("0")
