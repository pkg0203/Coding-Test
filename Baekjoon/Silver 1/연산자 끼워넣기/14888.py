"""
https://www.acmicpc.net/problem/14888

[ Back Tracking]
"""

def dfs(res,pl,mi,mu,di,walker=1):
    global Max,Min
    if walker == len(nums):
        if res > Max:
            Max = res
        if res < Min :
            Min = res
        return

    if pl:
        dfs(res+nums[walker],pl-1,mi,mu,di,walker+1)
    
    if mi:
        dfs(res-nums[walker],pl,mi-1,mu,di,walker+1)

    if mu:
        dfs(res*nums[walker],pl,mi,mu-1,di,walker+1)
    
    if di:
        dfs(int(res/nums[walker]),pl,mi,mu,di-1,walker+1)
    

import sys
import math

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
opperand = list(map(int,sys.stdin.readline().split()))
Max,Min = -math.inf,math.inf

dfs(nums[0],opperand[0],opperand[1],opperand[2],opperand[3])

sys.stdout.write(f"{Max}\n{Min}")