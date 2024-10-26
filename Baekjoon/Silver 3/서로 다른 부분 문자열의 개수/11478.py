"""
https://www.acmicpc.net/problem/11478
[ HashMap ]
"""

import sys

string = sys.stdin.readline().strip()

partial_string = {}

for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        substring = string[i:j]
        if not partial_string.get(substring):
            partial_string[substring] = 1

sys.stdout.write(f"{len(list(partial_string.keys()))}")