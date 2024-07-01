# https://www.acmicpc.net/problem/11402

# 아래의 블로그의 계산 예시를 보면 구현에 어렵지 않다.
# https://bowbowbow.tistory.com/2

# 그리고 modulo 계산 공식은 아래와 같다.
# https://sskl660.tistory.com/75

import sys

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

# N Combination K 를 구하는 함수
def get_comb(N, K):
    # N Combination K를 계산할 필요가 없을 때
    if N < K:
        return 0
    if N == 0 or K == 0:
        return 0
    # N Combination K를 계산할 필요가 있을 때
    # 계산할 때 6C3의 경우 (6*5*4 / 3*2*1) 로 분자와 분모를 나눠서 계산
    comb_val = 1
    # 분자 부분
    for factor in range(N, N - K, -1):
        comb_val *= factor
    # 분모 부분
    for divider in range(K, 0, -1):
        comb_val /= divider
    return int(comb_val)


answer = 0
N, K, prime = map(int, sys.stdin.readline().split())
N_array, K_array = get_coef(N, prime), get_coef(K, prime)
match_length(N_array, K_array)

# 배열을 역순으로 돌게 되는데 사실 꼭 그럴 필요는 없음
# 그냥 해보고 싶어서 구현해봄
for idx in range(len(N_array) - 1, -1, -1):
    comb_val = get_comb(N_array[idx], K_array[idx])
    if comb_val == 0:
        pass
    else:
        answer += comb_val
        answer %= prime
sys.stdout.write(f"{answer}")
