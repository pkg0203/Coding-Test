# https://www.acmicpc.net/problem/11653

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


number = int(sys.stdin.readline())

for prime in PRIMES:
    while number % prime == 0:
        number //= prime
        sys.stdout.write(f"{prime}\n")
    if number != 1:
        expand_prime_dict()
