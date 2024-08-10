# https://www.acmicpc.net/problem/5073

import sys

while True:
    lengths = list(map(int, sys.stdin.readline().split()))
    max_length = max(lengths)
    if lengths[0] == lengths[1] == lengths[2] == 0:
        break
    if 2 * max_length >= sum(lengths):
        sys.stdout.write("Invalid\n")
    elif lengths[0] == lengths[1] == lengths[2]:
        sys.stdout.write("Equilateral\n")
    elif (
        lengths[0] == lengths[1] or lengths[1] == lengths[2] or lengths[0] == lengths[2]
    ):
        sys.stdout.write("Isosceles\n")
    else:
        sys.stdout.write("Scalene\n")
