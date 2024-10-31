"""
https://www.acmicpc.net/problem/1735
[ Number Theory ]

최소 공배수를 활용하여 분수의 계산을 해준다
up은 분자를 나타내고, down은 분모를 나타낸다 ··· (1)

분자와 분모의 최대 공약수를 통해 계산된 분수가 기약분수인지 확인하고
기약분수가 아니라면 최대 공약수로 나눠준다 ··· (2)
"""

def GCD(a,b):
    if b>a:
        a,b=b,a
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def LCD(a,b):
    return a*b//GCD(a,b)

import sys

a,b=map(int,sys.stdin.readline().split())
c,d=map(int,sys.stdin.readline().split())

# (1)
lcd_val = LCD(b,d)
up = a*lcd_val//b+c*lcd_val//d
down = lcd_val
# (2)
gcd_val = GCD(up,down)
if gcd_val!=1:
    up//=gcd_val
    down//=gcd_val

sys.stdout.write(f"{up} {down}")