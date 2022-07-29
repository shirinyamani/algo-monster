
def search_unknown_size(reader, target):
    left = 0
    right = reader.next()
    while left < right:
        mid = (left + right) // 2
        if reader.get(mid) == target:
            return mid
        elif reader.get(mid) < target:
            left = mid + 1 
        else:
            right = mid - 1
    return -1


def search_unknown_size(arr, target):
    i = 1
    while ArrayReader.get(i) < target:
        i = i * 2
    return binary_search(arr, target, i // 2, i)

def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        mid = ArrayReader.get(mid)

        if arr[mid] <= target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

    else: return -1