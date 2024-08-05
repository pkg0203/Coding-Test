# https://www.acmicpc.net/problem/9063

import sys

T = int(sys.stdin.readline())
x_array=[]
y_array=[]
for testcase in range(T):
    x,y = map(int,sys.stdin.readline().split())
    x_array.append(x)
    y_array.append(y)
sys.stdout.write(f"{(max(x_array)-min(x_array))*(max(y_array)-min(y_array))}")