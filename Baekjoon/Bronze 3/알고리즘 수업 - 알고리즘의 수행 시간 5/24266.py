"""
https://www.acmicpc.net/problem/24266

[ Time Complexity ]

시간 복잡도는 O(n^3)이다 ··· (1)
"""
import sys

n = int(sys.stdin.readline())
# (1)
order = 3
sys.stdout.write(f"{n**3}\n{order}")
