import heapq
def largest(nums, k):
    heap = [] 
    for num in nums:
        heapq.heappush(heap, (-1 * num)) # -1 * num to make it a max heap

    largest = 0 # largest is the largest element in the heap
    for _ in range(k):
        largest = -1 * heapq.heappop(heap) 
    return largest