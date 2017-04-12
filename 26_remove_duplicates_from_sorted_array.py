#coding=utf8

def remove_duplicate(l):
    if not l:
        return 0
    j = 0
    for i in range(1, len(l)):
        if l[i] != l[j]:
            l[i], l[j+1] = l[j+1], l[i]
            j += 1
    return j+1

test_list = [1,2,2,3,3,3,4,5,6]
print(remove_duplicate(test_list))
print(test_list)
