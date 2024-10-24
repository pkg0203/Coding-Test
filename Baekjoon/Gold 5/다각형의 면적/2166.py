"""
https://www.acmicpc.net/problem/2166
[ Geometrics ]

보자마자 신발끈 공식 떠올랐다 링크는 아래에 첨부해두었다
https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D

다만 오목 다각형인 경우엔 오답이 되긴 한다

"""

import sys

N = int(sys.stdin.readline())
x = []
y = []
for _ in range(N):
    data = list(map(int,sys.stdin.readline().split()))
    x.append(data[0])
    y.append(data[1])
a,b = 0,0
for i in range(N) :
    a += x[i] * y[(i+1)%N]
    b += y[i] * x[(i+1)%N]

print(f"{round(abs(a-b)/2,1)}")