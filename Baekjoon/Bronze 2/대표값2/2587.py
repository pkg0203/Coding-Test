"""
https://www.acmicpc.net/problem/2587
[ Sorting ]

지난 코드에서 정렬을 직접해서 이번에는 메소드를 활용하기로 했다 ··· (1)

평균 = 합 / 개수이고 중앙값은 3번째 값이므로, index는 2이다 ··· (2)
"""

import sys

elements = []

for i in range(5) :
    elements.append(int(sys.stdin.readline()))
# (1)
elements.sort()
# (2)
sys.stdout.write(f"{sum(elements)//len(elements)}\n{elements[2]}")