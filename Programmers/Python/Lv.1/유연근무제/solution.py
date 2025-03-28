"""
https://school.programmers.co.kr/learn/courses/30/lessons/388351?language=python3

[ 시간 계산 ]
"""


def is_valid_work(sch, go):
    sch_h, go_h = sch // 100, go // 100
    sch_m, go_m = sch % 100, go % 100
    diff_h = sch_h - go_h
    diff_m = sch_m - go_m
    if diff_m < 0:
        diff_h -= 1
        diff_m += 60
    # 아예 일찍 온 경우
    if diff_h >= 0:
        return True
    # 10분 이내로 온 경우
    if diff_h == -1 and diff_m >= 50:
        return True
    return False


def is_weekday(n):
    if n % 7 == 6 or n % 7 == 0:
        return False
    return True


def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        all_valid = True
        for j in range(len(timelogs[i])):
            go_time = timelogs[i][j]
            today = startday + j
            if is_weekday(today):
                if not is_valid_work(schedules[i], go_time):
                    all_valid = False
                    break
        if all_valid:
            answer += 1
    return answer
