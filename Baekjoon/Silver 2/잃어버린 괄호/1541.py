"""
https://www.acmicpc.net/problem/1541

[ Greedy Algorithm ]

'-'를 기준으로 항을 전부 나눈다 ··· (1)

첫 번째 항의 값을 초기값으로 설정한다 ··· (2)

첫 번째 항 이후의 항은 최대한 뺀다 ··· (3)
"""

import sys

equation = sys.stdin.readline().rstrip()
# (1)
sections = equation.split('-')
answer = sections[0]

# (2)
try:
    answer = int(answer)
except:
    p_sections = answer.split('+')
    answer = int(p_sections[0])
    for i,p_sec in enumerate(p_sections):
        if i == 0 :
            continue
        answer += int(p_sec)
# (3)
for i,section in enumerate(sections):
    if i==0:
        continue
    nums = section.split('+')
    p_answer = int(nums[0])
    for i,num in enumerate(nums):
        if i == 0 :
            continue
        p_answer += int(num)

    answer -= p_answer

sys.stdout.write(f"{answer}")