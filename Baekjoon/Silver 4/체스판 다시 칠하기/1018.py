# https://www.acmicpc.net/problem/1018

import sys

START_B = "BW"
START_W = "WB"
LENGTH = 8


def count_chess(partial_chess):
    count_B = 0
    count_W = 0
    for i in range(LENGTH):
        for j in range(LENGTH):
            if partial_chess[i][j] != START_B[(i + j) % 2]:
                count_B += 1
            if partial_chess[i][j] != START_W[(i + j) % 2]:
                count_W += 1
    return min(count_B, count_W)


def find_sol(i=1, j=15):
    global answer
    partial_chess = []
    for row in range(LENGTH):
        partial_chess.append(input_chess[i+row][j : j + LENGTH])
    # update answer
    comp_answer = count_chess(partial_chess)
    answer = min(answer, comp_answer)

    # move position
    if j + LENGTH < M:
        find_sol(i, j + 1)
    elif i + LENGTH < N:
        find_sol(i + 1, j=0)


N, M = map(int, sys.stdin.readline().split())
input_chess = []
# 8 * 8 의 값이 initial value
answer = 64
for index in range(N):
    input_chess.append(list(sys.stdin.readline())[:M])
find_sol()
sys.stdout.write(f'{answer}')
