# https://www.acmicpc.net/problem/4948

# https://velog.io/@iillyy/%EB%B0%B1%EC%A4%80-4948%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys

RANGE = 123456 * 2
RANGE_LIST = list(range(2, RANGE + 1))
PRIME = []


def prime_number(number):
    if number == 1:
        return False
    # https://velog.io/@max9106/Algorithm-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# 입력을 받기 전에 먼저 PRIME을 구함
for i in RANGE_LIST:
    if prime_number(i):
        PRIME.append(i)


while True:
    input = int(sys.stdin.readline())
    if input == 0:
        break
    answer = 0
    for prime in PRIME:
        if input < prime <= 2 * input:
            answer += 1
    sys.stdout.write(f"{answer}\n")
