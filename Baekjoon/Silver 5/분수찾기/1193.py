# https://www.acmicpc.net/problem/1193

import sys

def sequential_sequence(i):
    if i<=0:
        return None
    else :
        return int(1+i*(i-1)/2)

N = int(sys.stdin.readline())
step=1
while True:
    if sequential_sequence(step)<=N<sequential_sequence(step+1):
        break
    else :
        step+=1
sum_of_a_b=step+1
if step%2==0:
    a=1
    b=sum_of_a_b-1
    for i in range(sequential_sequence(step),sequential_sequence(step+1)):
        if i ==N:
            break
        else :
            a+=1
            b-=1
else:
    a=sum_of_a_b-1
    b=1
    for i in range(sequential_sequence(step),sequential_sequence(step+1)):
        if i ==N:
            break
        else :
            a-=1
            b+=1
sys.stdout.write(f'{a}/{b}')
