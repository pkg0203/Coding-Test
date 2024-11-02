"""
https://www.acmicpc.net/problem/17103
[ Number Theory ]

에라토스테네스의 체를 활용한다

T를 입력받기 전에 소수들을 모두 구한다 ··· (1)

number에 대해 a가 소수이면서, (number-a)도 소수라면
이는 골드바흐 파티션에 해당 ··· (2)

순서가 바뀌었을 때, 같은 파티션이므로 a는 number의 절반까지만 순회 ··· (3)
"""
        

import sys
LIMIT = 1000000
PRIMES = []
sieve = [1 for _ in range(LIMIT+1)]
sieve[0] = 0
sieve[1] = 0

#(1)
for walker in range(2,LIMIT+1):
    if sieve[walker]:
        for i in range(walker+walker,LIMIT+1,walker):
            sieve[i]=0

T = int(sys.stdin.readline())

for testcase in range(T):
    answer = 0
    number = int(sys.stdin.readline())
    # (3)
    for walker in range(2,number//2+1):
        # (2)
        if sieve[walker] and sieve[number-walker]:
            answer +=1
    sys.stdout.write(f"{answer}\n")

