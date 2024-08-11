"""
https://www.acmicpc.net/problem/24267

[ Time Complexity ]

반복문이 3개이므로, 시간 복잡도는 O(n^3)이다 ··· (1)

총 연산량은 sigma(sigma(k)){k is 1 to n-2} 를 계산한 결과와 같다.
이는 메모장에 직접 쓰면서 규칙을 찾은 것이다.

이를 수학적으로 계산한 것을 count로 사용한다 ··· (2)

계산 방법은 Wolframalpha에 Sum[Sum[k,{k,1,n}],{n,1,x-2}] 을 입력하면 확인할 수 있다.
"""
import sys

n = int(sys.stdin.readline())
# (1)
order = 3
# (2)
count =(n-2)*(n-1)*n//6
sys.stdout.write(f"{count}\n{order}")