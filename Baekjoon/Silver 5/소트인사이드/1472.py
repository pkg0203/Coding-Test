"""
https://www.acmicpc.net/problem/1427
[ Sorting ]

당연히 이 코드를 한 번에 쓴 것은 아니고
안쪽부터 차근차근 생각하면서 쓰면 된다

각 문자열을 쪼개기 위해 string list로 입력을 받되,
개행문자가 있으므로 마지막 문자를 제외하고 받는다
숫자별로 정렬하기 원소를 int로 바꾸기 위해 list(map(int,string_list))를 사용하고
이제 int_list이므로 내림차순 정렬을 위해 sorted(int_list, reverse=True)를 사용한다 ··· (1)

join은 각 원소가 string이어야 하는데, 이를 다시 string으로 바꾸면 코드가 복잡해지므로
그냥 하나하나 출력해준다 ··· (2)
"""

import sys
# (1)
N = sorted(list(map(int,list(sys.stdin.readline())[:-1])),reverse=True)
# (2)
for number in N :
    sys.stdout.write(f"{number}")