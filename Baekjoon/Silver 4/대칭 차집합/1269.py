"""
https://www.acmicpc.net/problem/1269
[ HashMap ]

A의 원소를 inter_dict에 등록하고
B의 원소가 inter_dict에 있으면 교집합의 수를 늘린다
"""

import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

inter_dict = {}

for element in A:
    inter_dict[element] = 1

intersection = 0

for element in B:
    if inter_dict.get(element):
        intersection += 1
sys.stdout.write(f"{len(A)+len(B)-2*intersection}")
