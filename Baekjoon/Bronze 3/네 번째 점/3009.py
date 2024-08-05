# https://www.acmicpc.net/problem/3009

import sys

x_array=[]
y_array=[]

for case in range(3):
    x,y = map(int,sys.stdin.readline().split())
    if x in x_array:
        x_array.remove(x)
    else :
        x_array.append(x)

    if y in y_array:
        y_array.remove(y)
    else :
        y_array.append(y)

sys.stdout.write(f"{x_array[0]} {y_array[0]}")