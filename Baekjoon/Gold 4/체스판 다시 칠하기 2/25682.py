"""
https://www.acmicpc.net/problem/25682

[ Prefix Sum ]

B_board[i][j] : B로 시작하는 체스판에서 ~
W_board[i][j] : W로 시작하는 체스판에서 ~
(0,0) 부터 (i,j)까지 대각선으로 그었을 때, 체스판이 되기 위해
고쳐야 하는 수 ··· (1)

answer는 모든 체스판을 고쳐야 할 경우로 초기화 ··· (2)

Pattern_W와 일치하면 W_board[i-1][j] + W_board[i][j-1] - W_board[i-1][j-1] 을 수행하고
그렇지 않으면 이 값에 1을 더한다 ··· (3)
"""

PA_W = ("W", "B")
PA_B = ("B", "W")
import sys

N, M, K = map(int, sys.stdin.readline().split())
chess_board = []
# (1)
B_board = [[0 for j in range(M + 1)] for i in range(N + 1)]
W_board = [[0 for j in range(M + 1)] for i in range(N + 1)]
# (2)
answer = 2000*2000//2
for row in range(N):
    r = list(sys.stdin.readline().rstrip())
    chess_board.append(r)

for i, row in enumerate(chess_board):
    for j, val in enumerate(row):
        # (3)
        if val == PA_W[(i + j) % 2]:
            W_board[i + 1][j + 1] = W_board[i + 1][j] + W_board[i][j + 1] - W_board[i][j]
            B_board[i + 1][j + 1] = B_board[i + 1][j] + B_board[i][j + 1] - B_board[i][j] + 1
        else:
            W_board[i + 1][j + 1] = W_board[i + 1][j] + W_board[i][j + 1] - W_board[i][j] + 1
            B_board[i + 1][j + 1] = B_board[i + 1][j] + B_board[i][j + 1] - B_board[i][j]


for i in range(1,N+2-K):
    for j in range(1,M+2-K):
        B_board_sum = B_board[i+K-1][j+K-1] - B_board[i+K-1][j-1] - B_board[i-1][j+K-1] + B_board[i-1][j-1]
        W_board_sum = W_board[i+K-1][j+K-1] - W_board[i+K-1][j-1] - W_board[i-1][j+K-1] + W_board[i-1][j-1]
        answer = min(answer,B_board_sum,W_board_sum)

sys.stdout.write(f"{answer}")