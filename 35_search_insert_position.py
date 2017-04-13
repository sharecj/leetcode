#coding=utf8

def searchInsert(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) / 2
        print lo, hi, mid
        midval = nums[mid]
        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            return mid
        print lo, hi, mid
    print lo, hi, mid
    return lo
        
test_list = [1, 3, 4, 5]
print(searchInsert(test_list, 0))

