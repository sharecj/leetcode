#coding=utf8

def merge(l1, l2):
    ml = []
    l1_i = 0
    l2_i = 0
    for i in range(len(l1) + len(l2)):
        if l1_i > len(l1) - 1:
            ml.extend(l2[l2_i:])
            break
        elif l2_i > len(l2) - 1:
            ml.extend(l1[l1_i:])
            break

        if l1[l1_i] <= l2[l2_i]:
            ml.append(l1[l1_i])
            l1_i += 1
        else:
            ml.append(l2[l2_i])
            l2_i += 1

    return ml

test_l1 = [1, 3, 4, 5, 6, 12, 83, 232]
test_l2 = [1, 2, 3, 10, 16, 22, 99, 152, 333, 555, 777]

print(merge(test_l1, test_l2))
