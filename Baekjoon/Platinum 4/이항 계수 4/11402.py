# https://www.acmicpc.net/problem/11402

# 아래의 블로그의 계산 예시를 보면 구현에 어렵지 않다.
# https://bowbowbow.tistory.com/2

# 그리고 modulo 계산 공식은 아래와 같다.
# https://sskl660.tistory.com/75

import sys
# combination 계산은 library 쓰도록 합시다...
import math


# number를 prime에 대한 내림차순 계수를 구하는 함수
def get_coef(number, prime):
    array = []
    while number > 0:
        array.append(number % prime)
        number //= prime
    return array


# 두 배열의 길이가 안 맞을 때 맞춰주는 함수
# 사실 N이 K보다 크기 때문에 else문은 필요없긴 하다.
def match_length(N_array, K_array):
    len_N, len_K = len(N_array), len(K_array)
    while len_N != len_K:
        if len_N > len_K:
            K_array.append(0)
            len_K += 1
        else:
            N_array.append(0)
            len_N += 1
    return None


answer = 1
N, K, prime = map(int, sys.stdin.readline().split())
N_array, K_array = get_coef(N, prime), get_coef(K, prime)
match_length(N_array, K_array)
# print(N_array,K_array)
for idx in range(len(N_array)):
    comb_val = math.comb(N_array[idx], K_array[idx])
    # print(f"{N_array[idx]} C {K_array[idx]} = {comb_val}")
    if comb_val == 0:
        answer = 0
        break
    else:
        answer *= comb_val
        answer %= prime
sys.stdout.write(f"{answer}")
