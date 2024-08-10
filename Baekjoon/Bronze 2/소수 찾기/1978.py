# https://www.acmicpc.net/problem/1978

import sys

PRIMES = [2, 3, 5, 7]


# PRIME 확장 함수
def expand_prime_dict():
    walker = PRIMES[-1]
    while True:
        walker += 1
        max_walker = int(walker**0.5)
        is_divided = False
        for prime in PRIMES:
            # prime이 max_walker보다 크면 break
            if prime > max_walker:
                break
            # prime이 max_walker까지 walker를 못 나누면 append
            if walker % prime == 0:
                is_divided = True
                break
        if not is_divided:
            PRIMES.append(walker)
            break


T = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())
answer = 0
# number가 PRIME에 있으면 answer에 1을 더함
# number가 PRIME에 없으면
# 1. 가장 큰 PRIME보다 작으면 number는 PRIME이 아님
# 2. 가장 큰 PRIME보다 크면 PRIME을 확장함
for number in numbers:
    while True:
        if number <= PRIMES[-1]:
            if number in PRIMES:
                answer += 1
            break
        expand_prime_dict()
sys.stdout.write(f"{answer}")
