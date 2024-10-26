"""
https://www.acmicpc.net/problem/9184
[ Dynamic Programming ]

입력 받을 때마다 표를 채우면 index out이 발생할 우려가 있으므로

입력 받기 전에 dp표를 다 채우고 dp[a][b][c]를 출력한다

a,b,c 중 하나라도 20보다 크면 dp[20][20][20]을 참조하도록 한다
"""

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return dp[20][20][20]
    else :
        return dp[a][b][c]

def print_value(a,b,c,value):
    sys.stdout.write(f"w({a}, {b}, {c}) = {value}\n")

def fill_dp():
    if i>20 or j>20 or k>20:
        dp[i][j][k] = w[20][20][20]
    if i<j and j<k:
        dp[i][j][k] = w(i,j,k-1) + w(i,j-1,k-1) - w(i,j-1,k)
    else :
        dp[i][j][k] =w(i-1, j, k) + w(i-1, j-1, k) + w(i-1, j, k-1) - w(i-1, j-1, k-1)

import sys

dp = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]
dp[0][0][0] = 1
for i in range(21):
    for j in range(21):
        for k in range(21):
            fill_dp()
while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a==b==c==-1:
        break
    print_value(a,b,c,w(a,b,c))
