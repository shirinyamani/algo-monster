# approach 1: Dict/Counter
import collections

#Approach 1: Dict/Counter
def containDuplicates(nums):
    count = collections.Counter(nums)
    for num in nums:
        if count[num] > 1:
            return True
        else: False

#Approach 2: Set
def containDuplicates(nums):
    hash_set = set()
    for num in nums:
        if num in hash_set:
            return True
        hash_set.add(num)

    return False