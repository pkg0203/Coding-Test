# https://www.acmicpc.net/problem/11653

import sys


number = int(sys.stdin.readline())
walker = 2
while number != 1:
    if number % walker == 0:
        sys.stdout.write(f"{walker}\n")
        number /= walker
    else:
        walker += 1
