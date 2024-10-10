"""
https://www.acmicpc.net/problem/11054
[ Dynamic Programming ]

left_LIS[i] : i 번째 원소로 끝나는 점차 증가하는 부분 수열 ··· (1)

right_LDS[i] : i 번째 원소로 시작하는 점차 감소하는 부분 수열 ··· (2)

LIS 는 이미 풀었으므로 아래의 링크를 참조
https://github.com/pkg0203/Coding-Test/blob/main/Baekjoon/Silver%202/%EA%B0%80%EC%9E%A5%20%EA%B8%B4%20%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4/11053.py
··· (3)

LDS는 순회 순서를 반대로 해야한다
왜냐하면 반대로 순회하지 않으면 우측 초기값을 이미 계산된 것으로 반영하기 때문이다 ··· (4)

LIS와 LDS를 더해서 가장 긴 것이 가장 긴 바이토닉 수열이 되는데
가운데 1개가 겹치므로 1개 빼준다
ex ) 
선택된 LIS : 1 2 "3"
선택된 LDS : "3" 1 ··· (5)
"""

import sys

LEN = int(sys.stdin.readline())
elements = list(map(int, sys.stdin.readline().split()))

# (1)
left_LIS = [1 for _ in range(LEN)]
# (2)
right_LDS = [1 for _ in range(LEN)]

# (3)
for i in range(LEN):
    for j in range(i):
        if elements[j] < elements[i] :
            left_LIS[i] = max(left_LIS[i],left_LIS[j]+1)

# (4)
for i in range(LEN,-1,-1):
    for j in range(i+1,LEN):
        if elements[j] < elements[i] :
            right_LDS[i] = max(right_LDS[i],right_LDS[j]+1)

# (5)
dp = []
for i in range(LEN):
    dp.append(left_LIS[i]+right_LDS[i]-1)

sys.stdout.write(f"{max(dp)}")