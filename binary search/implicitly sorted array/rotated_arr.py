def search_rotared_arr(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
    
        # left portion is sorted
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1


        #right portion is sorted
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid -1

            else:
                left = mid + 1


    return -1
