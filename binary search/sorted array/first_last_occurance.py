# Approach 1
def search_range(arr, target):
    res = []
    if (arr.count(target) == 0):
        return [-1, -1]
    res.append(arr.index(target))
    for i in range(len(arr)-1,-1,-1):
        if (arr[i] == target):
            res.append(i)
            break

    return res


# Approach 2: Binary Search
def searchRange(nums, target):
    left = binSearch(nums, target, True)
    right = binSearch(nums, target, False)
    return [left, right]

# leftBias=[True/False], if false, res is rightBiased
def binSearch(nums, target, leftBias):
    l, r = 0, len(nums) - 1
    i = -1
    while l <= r:
        m = (l + r) // 2
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            i = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1
    return i