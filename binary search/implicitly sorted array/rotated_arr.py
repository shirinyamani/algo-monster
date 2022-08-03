def search_rotared_arr(arr, left, right, target):
    if not arr:
        return -1

    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] < arr[mid]: # left is normally ordered
            if arr[left] < target <= arr[mid]:
                return search_rotared_arr(arr, left, mid-1, target)
            
            else:
                return search_rotared_arr(arr, mid+1, right, target)

        elif arr[mid] < arr[right]: # right is normally ordered
            if arr[mid] < target <= arr[right]:
                return search_rotared_arr(arr, mid+1, right, target)

            else:
                return search_rotared_arr(arr, left, mid-1, target)

        else:
            if arr[left] == arr[mid]:
                if arr[right] != arr[mid]:
                    return search_rotared_arr(arr, mid+1, right, target)
                