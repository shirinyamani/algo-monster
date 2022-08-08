def min_sorted_arr(nums):
    res = nums[0]
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left]) #bc the nums[left] itself can be the min
            break

        mid = (left + right) // 2
        if nums[mid] >= nums[left]:
            left = mid + 1

        else:
            right = mid - 1

    return res
