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
        if self.last_index <= 0 :
            return -1
        else :
            self.st[self.last_index -1] = None
            self.last_index -= 1
            
    def empty(self) :
        if self.last_index == 0 :
            return 1
        else :
            return 0
        
    def is_pair(self, value) :
        if self.last_index <= 0 :
            return 0
        elif value == ')' and self.st[self.last_index -1] == '(':
            return 1
        elif value == '}' and self.st[self.last_index -1] == '{':
            return 1
        elif value == ']' and self.st[self.last_index -1] == '[':
            return 1
        else :
            return 0

def solution(array) :
    st = Stack1(len(array))
    for w in range(len(array)) :
        word = array[w]
        print(word , f'{w}/{len(array)}')
        if word == '(' or word == '{' or word == '[' :
            st.push(word)
        elif st.is_pair(word) :
            st.delete()
        else :
            print('!!!!!')
            return 'No'
        print(st.st)
    print(st.st, st.last_index)
    if st.empty :
        return 'Yes'
    else :
        return 'No'

if __name__ == '__main__' :
    T = int(sys.stdin.readline())
    for t in range(T) :
        ans = sys.stdin.readline()
        print(solution(ans))
        
            