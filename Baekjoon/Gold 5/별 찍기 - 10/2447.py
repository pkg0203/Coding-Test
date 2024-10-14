"""
https://www.acmicpc.net/problem/2447
[ Recursion ]

* 이 가득 채워진 배열을 초기화하고
이 배열에 구멍을 뚫는다 ··· (1)

N은 구멍을 뚫는 개수
i는 구멍을 처음 뚫을 행의 위치
j는 구멍을 처음 뚫는 열의 위치 ··· (2)

반복문을 통해 결국 N**2개의 구멍을 뚫게된다 ··· (3)

N이 1보다 크다는 조건은 base case (재귀함수 탈출 조건)
역할 수행 ··· (4)

현재 level의 구멍을 뚫었으니 다음 level (3으로 나눈 몫)의
상,하,좌,우, 좌상, 좌하, 우상, 우하를 재귀로 구현 ··· (5)
"""

import sys


def print_star():
    for i in range(N):
        for j in range(N):
            sys.stdout.write(f"{star[i][j]}")
        sys.stdout.write("\n")


def make_blank(N, i, j):
    # (3)
    for a in range(i, i + N):
        for b in range(j, j + N):
            star[a][b] = " "

    # (4)
    if N > 1:
        # (5)
        top = i - 2 * (N // 3)
        left = j - 2 * (N // 3)
        mid = j + (N // 3) 
        right = j + N + (N // 3)
        bottom = i + N + (N // 3)
        middle = i + (N // 3)
        # top left
        make_blank(N // 3, top, left)
        # top mid
        make_blank(N // 3, top, mid)
        # top right
        make_blank(N // 3, top, right)
        # middle left
        make_blank(N // 3, middle, left)
        # right
        make_blank(N // 3, middle, right)
        # bottom left
        make_blank(N // 3, bottom, left)
        # bottom mid
        make_blank(N // 3, bottom, mid)
        # bottom right
        make_blank(N // 3, bottom, right)


N = int(sys.stdin.readline())
# (1)
star = [["*" for i in range(N)] for j in range(N)]
# (2)
make_blank(N // 3, N // 3, N // 3)
print_star()
