"""
https://www.acmicpc.net/problem/10815
[ HashMap ]

inputs에 있는 값들이 cards에 있는지 확인한다
"""

import sys

def binary_search(key):
    left = 0
    right = N-1
    while left <= right:
        mid = (left+right) //2
        if cards[mid] == key :
            sys.stdout.write("1 ")
            return None
        elif  cards[mid] < key :
            left = mid + 1

        else :
            right = mid -1
    sys.stdout.write("0 ")

N = int(sys.stdin.readline())
cards = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
inputs = list(map(int,sys.stdin.readline().split()))

for input in inputs:
    binary_search(input)