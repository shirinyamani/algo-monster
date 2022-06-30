import collections


def informTime(n, headID, manager, informTime):
    subs = collections.defaultdict(list) # key: manager, value: list of employees
    for i, emp in enumerate(manager):
        subs[emp].append(i)

    stack = [[headID, 0]] # [manager, time]
    time = 0

    while stack: # while stack is not empty
        man, man_t = stack.pop()  
        time = max(time, man_t) # 

        for sub in subs[man]:
            stack.append([sub, man_t + informTime[man]])

    return time