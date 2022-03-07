import sys

class Stack1() :
    st = []
    last_index = 0
    
    def __init__(self, size=10000) :
        self.st = [None] * size 
        
    def push(self, value) :
        self.st[self.last_index] = value
        self.last_index += 1
    
    def pop(self) :
        if self.last_index <= 0 :
            return -1
        value = self.st[self.last_index - 1]
        self.st[self.last_index - 1] = None
        self.last_index -= 1
        return value
    
    def size(self) :
        return self.last_index
    
    def empty(self) :
        if self.last_index == 0 :
            return 1
        else :
            return 0
    
    def top(self) :
        if self.last_index <= 0 :
            return -1
        else :
            return self.st[self.last_index - 1]
        
if __name__ == "__main__" :
    N = int(sys.stdin.readline())
    stk = Stack1()
    for n in range(N) :
        ans = sys.stdin.readline().split()
        order = ans[0]
        if order == 'push' :
            stk.push(ans[1])
        elif order == 'pop' :
            print(stk.pop())
        elif order == 'size' :
            print(stk.size())
        elif order == 'empty' :
            print(stk.empty())
        elif order == 'top' :
            print(stk.top())