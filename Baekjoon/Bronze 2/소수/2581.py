# https://www.acmicpc.net/problem/2581

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


M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
mn_primes = []
while PRIMES[-1] < N:
    expand_prime_dict()

for prime in PRIMES:
    if M <= prime <= N:
        mn_primes.append(prime)

if mn_primes:
    sys.stdout.write(f"{sum(mn_primes)}\n")
    sys.stdout.write(f"{mn_primes[0]}")
else:
    sys.stdout.write("-1")
