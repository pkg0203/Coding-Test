"""
https://www.acmicpc.net/problem/10845
[ Queue ]
"""


import sys

N = int(sys.stdin.readline())
class Queue():
    def __init__(self) -> None:
        self.count = 0
        self.head = 0
        self.tail = 0
        self.queue = []

    def push(self,number):
        self.queue.append(number)
        self.tail += 1
        self.count += 1

    def front(self):
        if self.empty():
            return -1
        return self.queue[self.head]

    def back(self):
        if self.empty():
            return -1
        return self.queue[self.tail-1]
    
    def size(self):
        return self.count
    
    def pop(self):
        if self.empty():
            return -1
        self.head += 1
        self.count -= 1
        return self.queue[self.head-1]
    
    def empty(self) -> bool:
        return self.count == 0
     
q = Queue()

for _ in range(N):
    data = list(map(str,sys.stdin.readline().split()))
    if data[0] == "push":
        q.push(data[1])
    
    elif data[0] == "front":
        print(q.front())
    
    elif data[0] == "back" :
        print(q.back())

    elif data[0] == "pop" :
        print(q.pop())

    elif data[0] == "size" :
        print(q.size())

    elif data[0] == "empty" :
        if q.empty():
            print(1)
        else :
            print(0)