"""
https://www.acmicpc.net/problem/2981

[ Mathematics ]

a mod m ≡ b mod m 이라면
(a-b) mod m ≡ 0 이다
즉 임의의 두 값의 차이들을 모은 집합의 최대 공약수를 구하고
그 최대 공약수의 약수가 답이 된다.
"""
import sys

def gcd(a,b):
    if b>a:
        a,b=b,a
    if b==0:
        return a
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

N = int(sys.stdin.readline())
nums = []
diffs = set()

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

for i in range(N):
    for j in range(i+1,N):
        diffs.add(abs(nums[i]-nums[j]))
diffs = sorted(list(diffs))
gcd_ = 0

for i in range(len(diffs)):
    gcd_ = gcd(gcd_,diffs[i])

factors = set()

for num in range(1,int(gcd_**(0.5))+1):
    if gcd_%num == 0:
        factors.add(num)
        factors.add(gcd_//num)
factors.remove(1)
for factor in sorted(list(factors)):
    sys.stdout.write(f"{factor} ")

