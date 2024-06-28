# https://www.acmicpc.net/problem/2720

import sys

# 거스름돈에 사용될 동전들
COINS = [25, 10, 5, 1]
T = int(sys.stdin.readline())

for testcase in range(T):
    change = int(sys.stdin.readline())
    # 정답을 담을 배열 초기화
    answer = [0 for _ in range(len(COINS))]
    for coin in COINS:
        while change >= coin:
            # 25 센트의 COINS에서의 인덱스 0이고, 그에 맞게 answer 증가
            answer[COINS.index(coin)] += 1
            change -= coin
    # join은 str 밖에 연산할 수 없으므로, answer 배열의 원소를 str으로 변환
    sys.stdout.write(f"{' '.join(map(str,answer))}\n")
