# https://www.acmicpc.net/problem/9251

# DP란?
# https://hongjw1938.tistory.com/47
import sys

# 개행 문자 때문에 마지막은 빼고 담아야 함
A = sys.stdin.readline()[:-1]
B = sys.stdin.readline()[:-1]
LEN_A, LEN_B = len(A), len(B)

# dp_table initialize
dp_table = [[0] * (LEN_B + 1) for i in range(LEN_A + 1)]

for i in range(1, LEN_A + 1):
    for j in range(1, LEN_B + 1):
        if A[i - 1] == B[j - 1]:
            dp_table[i][j] = dp_table[i - 1][j - 1] + 1
        else:
            dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

answer = dp_table[LEN_A][LEN_B]
sys.stdout.write(f"{answer}")
