# https://www.acmicpc.net/problem/2903

import sys

A = [2, 3]

term = int(sys.stdin.readline())
while True:
    try:
        side = A[term]
        sys.stdout.write(f"{side**2}")
        break
    except:
        A.append(A[-1] + 2 ** (len(A) - 1))
