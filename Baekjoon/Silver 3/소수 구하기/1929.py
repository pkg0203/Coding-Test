# https://www.acmicpc.net/problem/1929

import sys


def is_prime(number):
    if number != 1:
        for walker in range(2, int(number**0.5) + 1):
            if number % walker == 0:
                return False
        return True
    # If number is 1
    return False


M, N = map(int, sys.stdin.readline().split())
for number in range(M, N + 1):
    if is_prime(number):
        sys.stdout.write(f"{number}\n")
