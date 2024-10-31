"""
https://www.acmicpc.net/problem/13241
[ Number Theory ]

브론즈 5의 최소공배수 문제와 풀이가 같다
"""

import sys

def GCD(a,b):
    if b>a:
        a,b=b,a
    while b!=0:
        r = a%b
        a=b
        b=r
    return a

def LCD(a,b):
    return a*b //GCD(a,b)

A,B = map(int,sys.stdin.readline().split())
sys.stdout.write(f"{LCD(A,B)}")