"""
https://www.acmicpc.net/problem/2740

[ Divide and Conquer ]
"""

import sys
A = []
N,M = map(int,sys.stdin.readline().split())

for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    A.append(row)

B = []
M,K = map(int,sys.stdin.readline().split())

for _ in range(M):
    row = list(map(int,sys.stdin.readline().split()))
    B.append(row)

result = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += A[i][k]*B[k][j]

for row in result:
    for val in row:
        sys.stdout.write(f"{val} ")
    sys.stdout.write('\n')