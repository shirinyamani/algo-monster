import collections

def sort_by_popularity(features, responses): 
    
    features_set = set(features)
    order = {word: i for i, word in enumerate(features)}
    freq = collections.defaultdict(int) # {word: freq}
    for r in responses:
        for word in set(r.split(' ')):
            if word in features_set:
                freq[word] += 1
    features.sort(key=lambda x: (-freq[x], order[x]))
    return features
