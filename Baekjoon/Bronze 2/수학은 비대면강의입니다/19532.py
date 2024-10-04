"""
https://www.acmicpc.net/problem/19532
[ Brute Force ]

연립 방정식을 그냥 풀어서 문자로 답을 구한다
답은 정수로 보장되므로 몫을 구해도 된다 ··· (1)

"""

import sys

a,b,c,d,e,f = map(int,sys.stdin.readline().split())

# (1)
x = ( c*e - b*f ) // ( a*e - d*b )
y = ( c*d - f*a ) // ( b*d - a*e)

sys.stdout.write(f"{x} {y}")