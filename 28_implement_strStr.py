#coding=utf8

def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:len(needle)+i] == needle:
            return i
    return -1

haystack = 'this is a test'
needle = 'is'
print(strStr(haystack, needle))
