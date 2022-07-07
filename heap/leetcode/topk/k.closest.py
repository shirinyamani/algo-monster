import heapq

def closestPoint(points, k):
    pts = [] #list of the points
    for x, y in points: #for each point in the list of points
        dist = (abs(x)**2) + (abs(y)**2)
        pts.append([dist, x, y]) #add the distance and the point to the list

    res = []
    heapq.heapify(pts) #convert the list to a heap
    for _ in range(k):
        dist, x, y = heapq.heappop(pts) #pop the top k points
        res.append([x,y]) #add the popped point to the list
    return res
