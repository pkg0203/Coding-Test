"""
https://www.acmicpc.net/problem/4779
[ Recursion ]

EOF 입출력 처리를 해준다 ··· (1)

N을 입력 받고서, 3^N 의 길이를 가지는 line을 생성한다 ··· (2)

재귀함수 cantor를 실행해서 길이의 1/3에 해당하는 가운데를 잘라낸다 ··· (3)

선분의 길이가 1인 경우 재귀함수를 탈출한다 ··· (4)

길이는 end - start인데 end가 index인 관계로 1을 더한다.
잘라낼 길이(cut_length)는 길이의 1/3이다
자르기 시작할 곳은 시작 + 잘라낼 길이
자르기를 마칠 곳은 끝 - 잘라낼 길이로 재귀함수를 구성 ··· (5)

마지막으로 좌측과 우측에 대해 재귀함수를 시행 ··· (6)

재귀함수를 마치고 None인 부분은 공백으로 출력한다
출력을 마치고 개행문자를 통해 줄을 바꿔준다 ··· (7)
"""

# (5)
def cantor(line,start,end):
    length = end - start + 1
    # (4)
    if length ==1:
        return None
    
    cut_length = length //3
    cut_start = start + cut_length
    cut_end = end - cut_length

    for idx in range(cut_start,cut_end+1):
        line[idx] = None

    # (6)
    cantor(line,start,cut_start-1)
    cantor(line,cut_end+1,end)

import sys

# (1)
while True:
    try :
        # (2)
        N = int(sys.stdin.readline())
        line =["-"] * (3**N)
        # (3)
        cantor(line,0,len(line)-1)
        # (7)
        for element in line:
            if element is None:
                sys.stdout.write(" ")
            else:
                sys.stdout.write(f"{element}")
        sys.stdout.write("\n")
    except :
        break