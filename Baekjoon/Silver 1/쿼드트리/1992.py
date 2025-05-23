"""
[ Divide and Conquer ]

푸는 방법은 아래와 완전히 같다

https://github.com/pkg0203/Coding-Test/commit/5fd8866c4a2d15b29974a6cb8fd462b928b2f641
"""

import sys

def solve(size,row=0,col=0):
    switch = True
    strt = paper[row][col]

    for i in range(row,row+size):
        for j in range(col,col+size):
            if paper[i][j] != strt:
                switch = False
                break

    if switch:
        sys.stdout.write(f"{strt}")


    else:
        sys.stdout.write("(")
        next_size = size//2
        solve(next_size,row,col)
        solve(next_size,row,col+next_size)
        solve(next_size,row+next_size,col)
        solve(next_size,row+next_size,col+next_size)
        sys.stdout.write(")")

N = int(sys.stdin.readline())
paper = []

for _ in range(N):
    row = list(sys.stdin.readline().rstrip())
    paper.append(row)
solve(N)