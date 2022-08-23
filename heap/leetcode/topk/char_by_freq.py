from collections import Counter
import heapq

def sort_char_by_freq(s):
    count = Counter(s)
    max_heap= []
    heapq.heapify(max_heap)

    for ch, freq in count.items():
        heapq.heappush(max_heap, [-freq, ch])
    
    res = ""
    while(len(max_heap)):
        freq, letter = heapq.heappop(max_heap)
        print(freq,letter)

        res += (letter * (-freq))
        print(res)

    return res







if __name__ == "__main__":
    print(sort_char_by_freq("loovXxvvve"))