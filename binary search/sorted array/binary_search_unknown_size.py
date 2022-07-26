
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