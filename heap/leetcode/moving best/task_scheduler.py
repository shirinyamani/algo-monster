import collections
import heapq

def taskscheduler(tasks, n):
    count = collections.Counter(tasks) #to count the most-least frequent tasks
    max_heap = [-cnt for cnt in count.values()] #to create a max heap
    heapq.heapify(max_heap) #to create a max heap

    time = 0
    q = collections.deque() #[conut/task, time to procceed]
    while max_heap or q:
        time += 1

        if not max_heap:
            time = q[0][1]

        else:
            cnt = 1 + heapq.heappop(max_heap)
            if cnt:
                q.append([cnt, time +n])

        if q and q[0][1] == time: #when return back to the task to procceed forward with it
            heapq.heappush(max_heap, q.popleft()[0])

    return time
