"""
https://school.programmers.co.kr/learn/courses/30/lessons/161990

[ Mathematics ]

"#"을 감싸는 최소한의 직사각형의 꼭짓점 좌표를 구하면 된다.

가장 위쪽에 있는 #을 찾고 이 점의 y좌표가 좌측 상단 꼭짓점의 y좌표가 된다 ··· (1)

마찬가지로 가장 좌측에 있는 #을 찾고 이 점의 x좌표가 좌측 상단 꼭짓점의 x좌표가 된다 ··· (2)

가장 우측에 있는 #을 찾고 이 점의 x좌표가 우측 하단 꼭짓점의 x좌표가 될 것 같지만
우측은 index를 1 더해야 한다. 문제 링크를 확인하길 바란다 ··· (3)

마찬가지로 가장 하단에 있는 #을 찾고 1을 더한 값이 우측 하단 꼭짓점의 y좌표가 된다 ··· (4)
"""


def solution(wallpaper):
    # (1)
    for i in range(len(wallpaper)):
        switch = False
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                upside = i
                switch = True
                break
        if switch:
            break
    # (4)
    for i in reversed(range(len(wallpaper))):
        switch = False
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                downside = i+1
                switch = True
                break
        if switch:
            break
    # (2)
    for j in range(len(wallpaper[0])):
        switch = False
        for i in range(len(wallpaper)):
            if wallpaper[i][j] == "#":
                leftside = j
                switch = True
                break
        if switch :
            break
    # (3)
    for j in reversed(range(len(wallpaper[0]))):
        switch = False
        for i in range(len(wallpaper)):
            if wallpaper[i][j] == "#":
                rightside = j+1
                switch = True
                break
        if switch :
            break
            
    return [upside,leftside,downside,rightside]