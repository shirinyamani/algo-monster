import collections

def numOfMinutes(n, headID, manager, informTime):
    """
    :type n: int
    :type headID: int
    :type manager: List[int]
    :type informTime: List[int]
    :rtype: int
    """
        
    subordinates = collections.defaultdict(list)
    for i, emp in enumerate(manager): subordinates[emp].append(i)
    
    stack = [[headID, 0]] 
    time = 0
        
    
    while stack: 
        man, man_time = stack.pop()
        time = max(time, man_time)
        
        for subordinate in subordinates[man]:
            stack.append([subordinate, man_time + informTime[man]])
        
    return time


if __name__ == "__main__":
    print(num)
        