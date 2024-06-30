# https://www.acmicpc.net/problem/2501

import sys

N, K = map(int, sys.stdin.readline().split())
factors = [1]
walker = 2
switch = True
while len(factors) < K:
    if walker > N:
        sys.stdout.write("0")
        switch = False
        break

    if N % walker == 0:
        factors.append(walker)
    walker += 1

if switch:
    sys.stdout.write(f"{factors[K-1]}")
