input01 = '''
    14
    push 1
    push 2
    top
    size
    empty
    pop
    pop
    pop
    size
    empty
    pop
    push 3
    empty
    top
'''

output01 = '''
    2
    2
    0
    2
    1
    -1
    0
    1
    -1
    0
    3
'''

input02 = '''
    7
    pop
    top
    push 123
    top
    pop
    top
    pop
'''

output02 = '''
    -1
    -1
    123
    123
    -1
    -1
'''