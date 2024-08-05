# https://www.acmicpc.net/problem/1085

import sys

x,y,w,h = map(int,sys.stdin.readline().split())
mx , my = w/2,h/2
result = 0
if x >= mx and y >= my:
    result = min(w-x,h-y)
elif x >= mx and y < my :
    result = min(w-x,y)
elif x < mx and y >=my :
    result = min(x,h-y)
else:
    result = min(x,y)
sys.stdout.write(f"{result}")