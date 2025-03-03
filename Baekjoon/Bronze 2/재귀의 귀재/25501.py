"""
https://www.acmicpc.net/problem/25501

[ Recursion ]

"""

def recursion(string,l,r,level=1):
    if l>=r:
        return 1,level
    elif string[l] != string[r]:
        return 0,level
    else:
        return recursion(string,l+1,r-1,level+1)


import sys

N = int(sys.stdin.readline())

for _ in range(N):
    string = sys.stdin.readline()[:-1]

    is_pal , count = recursion(string,0,len(string)-1)
    sys.stdout.write(f"{is_pal} {count}\n")