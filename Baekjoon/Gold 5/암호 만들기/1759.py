# https://www.acmicpc.net/problem/1759

import sys

VOWELS = "aeiou"


def print_answer():
    for element in answer:
        sys.stdout.write(f"{element}\n")


def is_valid_word(string_word):
    # 자음 수를 세기 위함
    consonant = 0
    # 모음이 있는지
    switch = False
    for character in string_word:
        if character in VOWELS:
            switch = True
        else:
            consonant += 1

    if switch:
        if consonant >= 2:
            return True
    return False


def find_answer(idx=0, partial_word=[]):
    global answer
    # Base case
    if len(partial_word) == LENGTH:
        string_word = "".join(partial_word)
        if is_valid_word(string_word) and not string_word in answer:
            answer.append(string_word)
    # Move Level
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
