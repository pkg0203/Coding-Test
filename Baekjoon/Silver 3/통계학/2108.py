"""
https://www.acmicpc.net/problem/2108

[ Statistics ]
"""

import sys

N = int(sys.stdin.readline())
freq = {}
nums = []
for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
    if freq.get(num):
        freq[num] += 1
    else:
        freq[num] = 1
nums.sort()

avg = round(sum(nums)/N)
mean = nums[N//2]
max_dict_val = max(freq.values())
freq_l = sorted([key for key,value in freq.items() if value == max_dict_val])
rang = nums[N-1] - nums[0]
freq_v = 0
if len(freq_l) > 1 :
    freq_v = freq_l[1]
else:
    freq_v = freq_l[0]

sys.stdout.write(f"{avg}\n")
sys.stdout.write(f"{mean}\n")
sys.stdout.write(f"{freq_v}\n")
sys.stdout.write(f"{rang}")
