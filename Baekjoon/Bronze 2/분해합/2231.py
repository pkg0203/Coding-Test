"""
https://www.acmicpc.net/problem/2231
[ Brute Force ]

1부터 시작하면 너무 오래 걸릴 것 같아 대충
N을 4정도로 나눈 몫에서 시작 
시작 값을 walker로 할당 ··· (1)

walker와 자리수의 합이 N이라면 walker가 답이므로 출력하고
반복문을 종료 ··· (2)

답을 찾지 못 한 경우에는 walker가 N보다 커지는데
이 경우엔 문제의 조건에 따라 0을 출력 ··· (3)

"""

import sys

N = int(sys.stdin.readline())
# (1)
walker = N //4

while walker < N :
    # (2)
    if walker + sum(map(int,list(str(walker)))) == N :
        sys.stdout.write(f"{walker}\n")
        break
    walker+=1

# (3)
if walker >= N :
    sys.stdout.write("0\n")