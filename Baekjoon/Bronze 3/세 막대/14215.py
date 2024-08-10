# https://www.acmicpc.net/problem/14215

import sys

# 길이를 입력으로 받음
lengths = list(map(int, sys.stdin.readline().split()))
while True:
    max_length = max(lengths)
    # 삼각형을 이루는지 확인
    if 2 * max_length < sum(lengths):
        break
    # 아니라면 가장 큰 값을 1 줄임
    max_idx = lengths.index(max_length)
    lengths[max_idx] -= 1

sys.stdout.write(f"{sum(lengths)}")
