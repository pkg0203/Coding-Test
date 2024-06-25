# https://www.acmicpc.net/problem/4948

# https://nyol.tistory.com/123

import sys

RANGE = 123456 * 2
PRIME_FILTER = [0] * 2 + [1] * (RANGE - 1)
PRIME = []


def binary_search(number):
    left = 0
    right = len(PRIME) - 1
    while left < right:
        mid = (left + right) // 2
        if PRIME[mid] == number:
            return True
        elif PRIME[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return False


# walker가 PRIME일 때 PRIME의 배수를 제거하는 함수
def update_filter(walker):
    for i in range(2 * walker, RANGE, walker):
        PRIME_FILTER[i] = 0


# number까지의 PRIME을 구하는 함수
def expand_filter(number):
    # initialize walker
    if PRIME:
        walker = PRIME[-1]
    else:
        walker = 2

    while walker <= number:
        if PRIME_FILTER[walker]:
            PRIME.append(walker)
            update_filter(walker)
        walker += 1

expand_filter(123456)
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for number in range(n + 1, 2 * n + 1):
        # 프라임에 있으면 패스
        # if number in PRIME 을 쓰면 너무 오래 걸린다.
        if binary_search(number):
            pass
        # 없으면 구한다.
        else:
            expand_filter(number)
    answer = sum(PRIME_FILTER[n + 1 : 2 * n + 1])
    sys.stdout.write(f"{answer}\n")
