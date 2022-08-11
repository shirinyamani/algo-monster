def shipwithinDays(self, weights, days):
    """
    :type weights: List[int]
    :type D: int
    :rtype: int
    """
    if days == 1:
        return sum(weights)

    def minCapacity(capacity):
        total,cur_day = 0, 1
        for w in weights:
            total += w

            if total > capacity:
                total = w
                cur_day += 1

                if cur_day > days:
                    return False

        return True

    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        if minCapacity(mid):
            right = mid
        else: left = mid + 1
    return left