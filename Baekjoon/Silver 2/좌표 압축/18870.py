"""
https://www.acmicpc.net/problem/18870
[ Sorting - Binary Search ]

중복을 압축하기 위해 HashMap을 사용한다 ··· (1)

key_list의 index가 압축된 결과이다 ··· (2)
"""

import sys


def binary_search(key):
    left = 0
    right = len(key_list)
    while left <= right:
        mid = (left + right) // 2
        value = key_list[mid]
        if value == key:
            return mid
        elif value < key:
            left = mid + 1
        else:
            right = mid - 1
    return 0


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
# (1)
num_dict = {}
for number in numbers:
    if num_dict.get(str(number)):
        num_dict[str(number)] += 1
    else:
        num_dict[str(number)] = 1

key_list = sorted(list(map(int, num_dict.keys())))
# (2)
for number in numbers:
    sys.stdout.write(f"{binary_search(number)} ")
