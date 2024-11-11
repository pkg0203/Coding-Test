"""
[ Combinatorics ]

math의 factorial을 활용
"""

import math
import sys

N = int(sys.stdin.readline())
sys.stdout.write(f"{math.factorial(N)}")