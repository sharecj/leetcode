#coding=utf8

def lcp(strs):
    if len(strs) < 1:
        return ''

    ss = strs[0]
    for i, c in enumerate(ss):
        for s in strs:
            if len(s) < i+1 or s[i] != c:
                return ss[:i]

test_strs = ['abcd', 'ab', 'abe', 'abfgh']
print(lcp(test_strs))
