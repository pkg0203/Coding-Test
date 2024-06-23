# https://www.acmicpc.net/problem/3003

import sys

RULE = {"KING": 1, "QUEEN": 1, "LOOK": 2, "BISHOP": 2, "KNIGHT": 2, "PAWN": 8}

inputs = list(map(int, sys.stdin.readline().split()))
answer = []
for idx in range(6):
    answer.append(list(RULE.values())[idx] - inputs[idx])
# answer의 element는 int이기 때문에 join을 사용하기 위해서 str으로 변환
sys.stdout.write(f"{' '.join(list(map(str,answer)))}")
