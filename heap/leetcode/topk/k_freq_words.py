from collections import Counter
import heapq
# Approach 0
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words) #{word:freq}
        maxHeap = []
        heapq.heapify(maxHeap)
        for word, freq in count.items():
            heapq.heappush(maxHeap, [-freq,word])
        
        res = []
        for i in range(k):
            out = heapq.heappop(maxHeap)
            res.append(out[1])
        return res

#Aprroach 1
def topKFrequent(words, k):
   counts = collections.Counter(words) #build a dictionary of words and their frequencies

   arr_to_be_converted = [(-count, word) for word, count in counts.items()] #convert the dictionary to a list of tuples

   heapq.heapify(arr_to_be_converted) #convert the arr to a heap

   return [heapq.heappop(arr_to_be_converted)[1] for _ in range(k)] #return the top k words


#Approach 2
def topKFrequent(words, k):
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1

        else:
            word_freq[word] += 1

    min_heap = []

    for word, freq in word_freq.items():
        heapq.heappush(min_heap, (freq, word))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    res = []
    while min_heap:
        w = heapq.heappop(min_heap)
        res.append(w[1])

    return res[::-1]
