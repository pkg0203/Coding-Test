"""
https://www.acmicpc.net/problem/1780

[ Divide and Conquer ]

"""


def solve(size, r=0, c=0):
    global zero, one, m_one
    is_all_same = True
    strt = paper[r][c]
    for i in range(r, r + size):
        for j in range(c, c + size):
            if paper[i][j] != strt:
                is_all_same = False
                break

        if not is_all_same:
            break

    if is_all_same:
        if strt == 0:
            zero += 1
        elif strt == 1:
            one += 1
        elif strt == -1:
            m_one += 1
    
    else:
        next_size = size//3
        for a in range(3):
            for b in range(3):
                solve(next_size,r+a*next_size,c+b*next_size)


import sys

N = int(sys.stdin.readline())
paper = []
zero, one, m_one = 0, 0, 0

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    paper.append(row)

solve(N)
sys.stdout.write(f"{m_one}\n{zero}\n{one}")
