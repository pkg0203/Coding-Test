"""
[ Divide and Conquer ]
"""

import sys

def solve(size,row=0,col=0):
    global w,b
    switch = True
    strt = paper[row][col]

    for i in range(row,row+size):
        for j in range(col,col+size):
            if paper[i][j] != strt:
                switch = False
                break
        if not switch:
            break

    if switch:
        if strt:
            b+=1
        else:
            w+=1

    else:
        next_size = size//2
        solve(next_size,row,col)
        solve(next_size,row+next_size,col)
        solve(next_size,row,col+next_size)
        solve(next_size,row+next_size,col+next_size)


N = int(sys.stdin.readline())
w,b = 0,0
paper = []

for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    paper.append(row)

solve(N)
sys.stdout.write(f"{w}\n{b}")