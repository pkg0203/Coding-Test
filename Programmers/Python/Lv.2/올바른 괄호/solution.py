class Stack():
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        if len(self.items)==0:
            return None
        else:
            return self.items.pop()

def solution(s):
    switch = True
    stack=Stack()
    for string in s:
        if string =='(':
            stack.push(1)
        elif string==')':
            if len(stack.items)==0:
                switch=False
                break
            else :
                stack.pop()
    if stack.items:
        switch=False
    return switch