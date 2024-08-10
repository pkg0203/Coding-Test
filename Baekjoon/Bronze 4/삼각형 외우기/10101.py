# https://www.acmicpc.net/problem/10101

import sys

angles = []
for _ in range(3):
    angles.append(int(sys.stdin.readline()))

if sum(angles) != 180:
    sys.stdout.write("Error")
else:
    if angles[0] == angles[1] == angles[2] == 60:
        sys.stdout.write("Equilateral")
    elif angles[0] == angles[1] or angles[0] == angles[2] or angles[1] == angles[2]:
        sys.stdout.write("Isosceles")
    else:
        sys.stdout.write("Scalene")
