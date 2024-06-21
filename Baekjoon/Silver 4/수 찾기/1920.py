# https://www.acmicpc.net/problem/1920

import sys

def binary_search(array,key):
    left = 0
    right = len(array)-1
    while left<=right:
        mid = (left+right)//2
        if array[mid]<key:
            left=mid+1
        elif array[mid]>key:
            right=mid-1
        else:
            return 1
    return 0

N = int(sys.stdin.readline())
array=sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
keys=list(map(int,sys.stdin.readline().split()))
for key in keys:
    sys.stdout.write(f'{binary_search(array,key)}\n')