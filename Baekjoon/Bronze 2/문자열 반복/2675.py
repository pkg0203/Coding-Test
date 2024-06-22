# https://www.acmicpc.net/problem/2675

import sys

T = int(sys.stdin.readline())
for testcase in range(T):
    times, string = map(str, sys.stdin.readline().split())
    for index in range(len(string)):
        for i in range(int(times)):
            sys.stdout.write(f"{string[index]}")
    sys.stdout.write("\n")
