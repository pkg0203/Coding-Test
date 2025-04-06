"""
https://www.acmicpc.net/problem/11660

[ Prefix Sum ]

sum_board[i][j] = (1,1) ~ (i,j) 까지의 합
"""

import sys

N, M = map(int, sys.stdin.readline().split())
num_board = []
sum_board = [[0 for j in range(N)] for i in range(N)]

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    num_board.append(row)

# initialize
for i, row in enumerate(num_board):
    if i==0:
        sum_board[i][0] = row[0]
        for j,num in enumerate(row):
            if j:
                sum_board[i][j] = sum_board[i][j-1] + num
    else:
        sum_board[i][0] = row[0] + sum_board[i-1][0]

for i, row in enumerate(num_board):
    for j,num in enumerate(row):
        if i !=0 and j!= 0:
            sum_board[i][j] = num + sum_board[i-1][j] + sum_board[i][j-1] - sum_board[i-1][j-1]

for _ in range(M):
    result = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1==y1==1:
        result = sum_board[x2-1][y2-1]
    elif x1==1:
        result = sum_board[x2-1][y2-1] - sum_board[x2-1][y1-2]
    elif y1==1:
        result = sum_board[x2-1][y2-1] - sum_board[x1-2][y2-1]
    else:
        result = sum_board[x2-1][y2-1] - sum_board[x1-2][y2-1] - sum_board[x2-1][y1-2] + sum_board[x1-2][y1-2]
    sys.stdout.write(f"{result}\n")
