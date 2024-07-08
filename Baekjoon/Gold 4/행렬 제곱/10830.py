# https://www.acmicpc.net/problem/10830

import sys
import copy


def multiply(a_matrix, b_matrix):
    new_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_matrix[i][j] += a_matrix[i][k] * b_matrix[k][j]
            new_matrix[i][j] %= 1000
    return new_matrix


def print_matrix(result):
    for i in range(N):
        sys.stdout.write(f"{' '.join(map(str,result[i]))}\n")


N, power = map(int, sys.stdin.readline().split())
matrix = []
for idx in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
mat_expo = 1
result = copy.deepcopy(matrix)

while mat_expo < power:
    if 2 * mat_expo <= power:
        result = multiply(result, result)
        mat_expo *= 2
    else:
        result = multiply(result, matrix)
        mat_expo += 1
print_matrix(result)
