# https://www.acmicpc.net/problem/4948

import sys

PRIME = [2, 3, 5, 7, 11, 13]


def expand_prime_list():
    walker = PRIME[-1] + 1
    while True:
        max_comp = int(walker**0.5)
        switch = True
        for comp in PRIME:
            if comp > max_comp:
                break
            elif walker % comp == 0:
                switch = False
                break
        if switch:
            PRIME.append(walker)
            break
        walker += 1


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    answer = 0
    for number in range(n + 1, 2 * n + 1):
        while True:
            # It's Prime #
            if number in PRIME:
                answer += 1
                break
            # It isn't Prime #
            elif number < PRIME[-1]:
                break
            else:
                expand_prime_list()
    sys.stdout.write(f"{answer}\n")
