import sys

class Stack1() :
    st = []
    last_index = 0
    
    def __init__(self, size=10000) :
        self.st = [None] * size 
    
    def push(self, value) :
        self.st[self.last_index] = value
        self.last_index += 1
    
    def delete(self) :
        self.st[self.last_index -1] = None
        self.last_index -= 1
    
    def sum(self) :
        return sum(self.st[:self.last_index])

if __name__ == '__main__' :
    K = int(sys.stdin.readline())
    stk = Stack1(K)
    for k in range(K) :
        ans = int(sys.stdin.readline())
        if ans == 0 :
            stk.delete()
        else :
            stk.push(ans)
    print(stk.sum())