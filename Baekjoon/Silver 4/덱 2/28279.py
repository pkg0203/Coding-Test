"""
https://www.acmicpc.net/problem/28279
[ Deque ]

from collections import deque
해도 되는데, 저번에 그렇게 했으니 이번엔 구현해보고자 한다
"""

class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.previous = None

    def delete_node(self):
        self.value = None
        self.next = None
        self.previous = None

class CustomDeq():
    def __init__(self) -> None:
        self.count = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.count == 0

    def add_left(self,value):
        node = Node(value)
        if self.count != 0 :
            node.next = self.head
            self.head.previous = node
            self.head = node
        else :
            self.head = node
            self.tail = node
        self.count +=1

    def add_right(self,value):
        node = Node(value)
        if self.count != 0 :
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        else :
            self.head = node
            self.tail = node
        self.count +=1

    def show_left(self):
        return -1 if self.is_empty() else self.head.value

    def show_right(self):
        return -1 if self.is_empty() else self.tail.value

    def pop_left(self):
        if self.is_empty():
            return -1
        else :
            del_node = self.head
            self.head = del_node.next
            self.count -= 1
            return_value = del_node.value
            del_node.delete_node()
            return return_value
    
    def pop_right(self):
        if self.is_empty():
            return -1
        else :
            del_node = self.tail
            self.tail = del_node.previous
            self.count -= 1
            return_value = del_node.value
            del_node.delete_node()
            return return_value



import sys

deq = CustomDeq()
N = int(sys.stdin.readline())

for _ in range(N):
    data = list(map(int,sys.stdin.readline().split()))
    if data[0] == 1 :
        deq.add_left(data[1])
    if data[0] == 2 :
        deq.add_right(data[1])
    if data[0] == 3 :
        sys.stdout.write(f"{deq.pop_left()}\n")
    if data[0] == 4 :
        sys.stdout.write(f"{deq.pop_right()}\n")
    if data[0] == 5:
        sys.stdout.write(f"{deq.count}\n")
    if data[0] == 6:
        sys.stdout.write("1\n" if deq.is_empty() else "0\n")
    if data[0] == 7:
        sys.stdout.write(f"{deq.show_left()}\n")
    if data[0] == 8:
        sys.stdout.write(f"{deq.show_right()}\n")