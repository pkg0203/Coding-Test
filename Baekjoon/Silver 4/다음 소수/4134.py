"""
https://www.acmicpc.net/problem/4134
[ Number Theory ]

같아도 된다는 조건을 못 봤다
0도 포함인 것을 못 봤다

https://github.com/pkg0203/Coding-Test/blob/main/Baekjoon/Silver%202/%EB%B2%A0%EB%A5%B4%ED%8A%B8%EB%9E%91%20%EA%B3%B5%EC%A4%80/4948.py
"""

def is_prime(number):
    if number <= 1 :
        return False
    else:
        for i in range(2,int(number**0.5)+1):
            if number%i==0:
                return False
    return True

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    number = int(sys.stdin.readline())
    walker = number
    while True:
        if is_prime(walker):
            sys.stdout.write(f"{walker}\n")
            break
        else:
            walker +=1