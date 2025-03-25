"""
https://www.acmicpc.net/problem/2580

[ Back Tracking ]

DFS로 모든 index를 다 돌면 비효율적이기 때문에
0에 해당하는 index만 저장해둔다 ··· (1)

Row, Column, Box에 대해서 겹치지 않는다면,
유망하므로 Back Tracking을 시행 ··· (2)

모든 0을 다 채웠다면 print를 한다 ··· (3)

다만 결과가 여러 나와도 Back Tracking을 하는 일이 없도록
print 이후에 강제 종료한다 ··· (4)
"""

import sys

SUDOKU = []
BL_IDX = []
CAND = [i + 1 for i in range(9)]

def print_result():
    global SUDOKU
    for row in SUDOKU:
        for ele in row:
            sys.stdout.write(f"{ele} ")
        sys.stdout.write("\n")


def check_col(num, j):
    global SUDOKU
    for row in range(9):
        if SUDOKU[row][j] == num:
            return False
    return True


def check_row(num, i):
    global SUDOKU
    for col in range(9):
        if SUDOKU[i][col] == num:
            return False
    return True


def check_box(num, i, j):
    global SUDOKU
    ith, jth = i // 3, j // 3
    for a in range(3 * ith, 3 * ith + 3):
        for b in range(3 * jth, 3 * jth + 3):
            if SUDOKU[a][b] == num:
                return False
    return True


def solve(lv=0):
    global SUDOKU, BL_IDX
    if lv == len(BL_IDX):
        # (3)
        print_result()
        # (4)
        exit()

    i, j = BL_IDX[lv][0], BL_IDX[lv][1]
    # (2)
    for num in CAND:
        if check_box(num, i, j) and check_col(num, j) and check_row(num, i):
            SUDOKU[i][j] = num
            solve(lv + 1)
            SUDOKU[i][j] = 0


for _ in range(9):
    input = list(map(int, sys.stdin.readline().split()))
    # (1)
    for idx in range(9):
        if input[idx] == 0:
            BL_IDX.append([_, idx])
    SUDOKU.append(input)

solve()
