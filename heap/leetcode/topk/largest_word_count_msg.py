from matplotlib import collections

#Approach 1
def largestWordCount(messages, senders):
    d = {} 
    res = []

    for i in range(len(messages)):
        if senders[i] not in d:
            d[senders[i]] = len(messages[i].split())

        else:
            d[senders[i]] += len(messages[i].split())
    x = max(d.values())

    for k, v in d.items():
        if v == x:
            res.append(k)

    if len(res) == 1:
        return res[0]

    else: 
        res = sorted(res)[::-1]
        return res[0]




#Approach 2
def largestWordCount(messages, senders):

    counts = collections.Counter()
    for m, s in zip(messages, senders):
        counts[s] += m.count(' ') + 1

    largestCount, largestSender = 0, ""
    for sender, count in counts.items():
        if count > largestCount or (count == largestCount and sender > largestSender):
            largestCount, largestSender = count, sender

    return largestSender
