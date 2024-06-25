# https://www.acmicpc.net/problem/2738

import sys

N, M = map(int, sys.stdin.readline().split())

A, B = [], []

# result matrix
C = [[0 for i in range(M)] for j in range(N)]

# input A matrix
for row in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

# input B matrix
for row in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

# Evaluate 'C = A + B'
for row in range(N):
    for col in range(M):
        C[row][col] = A[row][col] + B[row][col]

# Print C matrix per row
for row in range(N):
    sys.stdout.write(f"{' '.join(map(str,C[row]))}\n")
