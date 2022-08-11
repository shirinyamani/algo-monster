def shipwithinDays(self, weights, D):
    """
    :type weights: List[int]
    :type D: int
    :rtype: int
    """
    def binary_search(left, right):
        if left > right:
            return 0
        mid = (left + right) // 2
        if sum(weights[:mid]) > D:
            return binary_search(left, mid - 1)
        elif sum(weights[:mid]) < D:
            return binary_search(mid + 1, right)
        else:
            return mid
    return binary_search(1, len(weights))