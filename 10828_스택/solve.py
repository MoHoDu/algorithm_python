import sys

N = int(sys.stdin.readline())
st = []
for n in range(N) :
    ans = sys.stdin.readline().split()
    order = ans[0]
    if order == 'push' :
        st.append(ans[1])
    if order == 'pop' :
        if len(st) == 0 :
            print(-1)
        else :
            print(st[-1])
            st.pop()
    if order == 'size' :
        print(len(st))
    if order == 'empty' :
        if len(st) == 0 :
            print(1)
        else :
            print(0)
    if order == 'top' :
        if len(st) == 0 :
            print(-1)
        else :
            print(st[-1])
