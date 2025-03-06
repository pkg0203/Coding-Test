"""
https://school.programmers.co.kr/learn/courses/30/lessons/250137

[ Implementaion ]
"""

def is_alive(health):
    return health > 0

def solution(bandage, health, attacks):
    max_hp,cur_hp = health,health
    g_time,h_time,walker = 0,0,0
    need_time,turn_heal,add_heal = bandage[0],bandage[1],bandage[2]
    while is_alive(cur_hp) and walker < len(attacks):
        if g_time == attacks[walker][0]:
            cur_hp -= attacks[walker][1]
            walker += 1
            h_time = 0
            
        else :
            h_time += 1
            cur_hp += turn_heal
            if h_time == need_time :
                cur_hp += add_heal
                h_time = 0
            
            if cur_hp > max_hp:
                cur_hp = max_hp
            
        g_time += 1
    
    if cur_hp >0:
        return cur_hp
    return -1