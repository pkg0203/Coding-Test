# https://www.acmicpc.net/problem/9506

import sys


def is_perfect_number(N):
    global factors
    max_walker = int(N**0.5)
    for i in range(2, max_walker + 1):
        if N % i == 0:
            factors.append(i)
            factors.append(N // i)
    return sum(factors) == N


def show_factors():
    factors.sort()
    # 시작 부분
    sys.stdout.write(f"{N} = 1")
    # +로 연결되는 부분
    for idx in range(1, len(factors)):
        sys.stdout.write(f" + {factors[idx]}")
    # 줄 바꿈
    sys.stdout.write("\n")


while True:
    N = int(sys.stdin.readline())
    # N is -1
    if N == -1:
        break
    # N is not -1
    factors = [1]
    if is_perfect_number(N):
        show_factors()
    else:
        sys.stdout.write(f"{N} is NOT perfect.\n")
