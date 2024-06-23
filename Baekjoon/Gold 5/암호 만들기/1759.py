# https://www.acmicpc.net/problem/1759

import sys

VOWEL = ["a", "e", "i", "o", "u"]

def print_answer():
    for element in answer:
        sys.stdout.write(f'{element}\n')

def exist_vowel(string_word):
    ret = False
    for idx in range(5):
        if VOWEL[idx] in ''.join(string_word):
            ret = True
    return ret

def find_answer(idx=0, partial_word=[]):
    global answer
    # Base case
    if len(partial_word) == LENGTH:
        string_word = ''.join(partial_word)
        if exist_vowel(string_word) and not string_word in answer:
            answer.append(string_word)
    if idx < CHAR:
        # Add Character
        partial_word.append(candidate[idx])
        find_answer(idx + 1, partial_word)
        partial_word.pop()
        # Don't add Character
        find_answer(idx + 1, partial_word)


LENGTH, CHAR = map(int, sys.stdin.readline().split())
candidate = sorted(list(sys.stdin.readline().split()))
answer = []
find_answer()
print_answer()
