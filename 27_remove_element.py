#coding=utf8

def remove_element(l, val):
    start = 0
    end = len(l) - 1
    while start <= end:
        while start < len(l) and l[start] != val :
            start += 1
        while end >= 0 and l[end] == val:
            end -= 1
        if start < end:
            l[start], l[end] = l[end], l[start]
    return start

test_list = [2,3,3,2,4,5,3]
print(remove_element(test_list, 3))
print(test_list)

test_list = [3,3]
print(remove_element(test_list, 2))
print(test_list)

test_list = [2]
print(remove_element(test_list, 3))
print(test_list)

