# dic/ counter for couting the elmnt-freq
# heap for efficinecy
from collections import Counter
import heapq

def top_k_element(nums, k):
    count = Counter(nums) #{elmnt: freq}
    heap = []
    heapq.heapify(heap)
    for elm, freq in count.items():
        heapq.heappush(heap, [-freq, elm])
    
    res = []
    for i in range(k):
        out = heapq.heappop(heap)
        res.append(out[1])
    return res
        

if __name__ == "__main__":
    print(top_k_element([1,1,1,2,2,3], 2))
