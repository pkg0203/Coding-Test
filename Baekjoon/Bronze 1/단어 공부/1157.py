# https://www.acmicpc.net/problem/1157
# ----------------------------------
# How to check Dictionary key exists
# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
# ----------------------------------
import sys

count_dict = {}
max_char = []
word = sys.stdin.readline()[:-1]
# Count character
for char in word:
    if char.upper() in count_dict.keys():
        count_dict[char.upper()] += 1
    else:
        count_dict[char.upper()] = 1
# Evaluate Max Value of Character
max_val = max(count_dict.values())
for key in count_dict:
    if count_dict[key] == max_val:
        max_char.append(key)
# Check Whether Character is duplicated
if len(max_char) != 1:
    sys.stdout.write("?")
else:
    sys.stdout.write(f"{max_char[0]}")
