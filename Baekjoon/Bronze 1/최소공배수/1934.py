"""
https://www.acmicpc.net/problem/1934
[ Number Theory ]

최소 공배수 = 두 수의 곱 / 최대공약수
를 이용
"""

def gcd(a,b):
    if b>a:
        a,b = b,a
    while b!=0:
        r = a%b
        a=b
        b=r
    return a

def lcd(a,b):
    return a*b // gcd(a,b)
        
import sys

T = int(sys.stdin.readline())

for testcase in range(T):
    a,b = map(int,sys.stdin.readline().split())
    sys.stdout.write(f"{lcd(a,b)}\n")