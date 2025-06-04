"""
https://www.acmicpc.net/problem/10830

[ Divide and Conquer ]
이전에 풀었던 '이항 계수 3'과 크게 다르지 않다 
다만 이 때 answer는 1이 아닌 Identity Matrix로 초기화 해야 한다 ··· (1)

입력을 모두 받고서 answer로 바로 받아준다 ··· (2)
"""

def mat_square(A,B):
    # (1)
    answer = [[1 if i==j  else 0 for j in range(N)] for i in range(N)]
    while B:
        if B%2==1:
            answer = multi(A,answer)

        A = multi(A,A)
        B//=2
    return answer

def multi(mat_a,mat_b):
    answer = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                answer[i][j] += mat_a[i][k]*mat_b[k][j]
            answer[i][j] %= R
    return answer

import sys

# (2)
N,B = map(int,sys.stdin.readline().split())
A = []
R = 1000
for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    A.append(row)
answer = mat_square(A,B)
#answer = multi(A,A)

for row in answer:
    for val in row:
        sys.stdout.write(f"{val} ")
    sys.stdout.write("\n")