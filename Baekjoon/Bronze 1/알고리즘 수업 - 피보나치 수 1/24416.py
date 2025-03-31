"""
https://www.acmicpc.net/problem/24416

[ Dynamic Programming ]
"""

import sys

n = int(sys.stdin.readline())

rec = [0,1,1]
while True:
    try :
        rec[n]
        break
    except:
        rec.append(rec[-1]+rec[-2])

dp = [0,0,0]
while True:
    try :
        dp[n]
        break
    except :
        dp.append(dp[-1]+1)
sys.stdout.write(f"{rec[n]} {dp[n]}")