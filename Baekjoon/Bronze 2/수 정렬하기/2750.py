"""
https://www.acmicpc.net/problem/2750
[ Sorting ]

elements.sort(reverse=True) 를 이용해서 한 방에 끝낼 수도 있지만
그럴거면 이 문제 풀 이유가 없긴 하다고 생각해서 직접 bubble sort로 구현했다.
"""

import sys

def sort(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j] :
                array[i] , array[j] = array[j] , array[i]

def print_elements(array):
    for element in array:
        sys.stdout.write(f"{element}\n")

N = int(sys.stdin.readline())
elements = []

for i in range(N):
    elements.append(int(sys.stdin.readline()))
sort(elements)
print_elements(elements)