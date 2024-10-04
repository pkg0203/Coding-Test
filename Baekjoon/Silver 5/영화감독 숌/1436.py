"""
https://www.acmicpc.net/problem/1436
[ Brute Force ]

간단하게 N번째가 movies에 있으면 출력하고
없으면 movies를 확장한다

movies에 N번째가 없다면 ··· (1)

movies의 마지막 원소에 1 더한 것부터 시작 ··· (2)

666이 있는지 확인한다 ··· (3)

없으면 1을 더하며 계속 확인 ··· (4)

while 문을 탈출하면 N번째 영화가 movies에 있게 되므로
출력한다. 또한 N이 3이하라면 while문을 돌지 않는다 ··· (5)
"""

import sys

movies = [666,1666,2666]

N = int(sys.stdin.readline())
# (1)
while len(movies) < N :
    # (2)
    walker = movies[-1] + 1
    while True :
        # (3)
        if "666" in str(walker):
            movies.append(walker)
            break
        # (4)
        else :
            walker +=1

# (5)
sys.stdout.write(f"{movies[N-1]}\n")