#coding=utf8

test_str = '[(({[]{}}))]'
test_str2 = '[(({[]{}}))]]'

def opposite(c):
    d = {'(': ')', '[': ']', '{': '}'}
    return d[c]

def valid(string):
    stack = []
    for c in string:
        if len(stack) < 1:
            stack.append(c)
        else:
            if opposite(stack[-1]) == c:
                stack.pop()
            else:
                stack.append(c)

    return False if stack else True

print(valid(test_str))
print(valid(test_str2))
