"""
https://www.acmicpc.net/problem/11401

[ Divide and Conquer ]

아래의 사이트를 참고하면 좋다

https://deepdata.tistory.com/370

"""

def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
        result %= R
    return result

def power(a,n):
    result = 1
    while n:
        if n%2==1 :
            result *= a

        a*=a
        a%=R
        n//=2
    return result

import sys
R = 1000000007
N,K = map(int,sys.stdin.readline().split())
answer = factorial(N)*power(factorial(N-K)*factorial(K),R-2) % R
sys.stdout.write(f"{answer}")
