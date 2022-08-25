import collections

def sort_features(features, responses):
    # freq ---> default dict (list)   features --- responses
    # response split 
    # order ---> i , word (enumerate)
    feature_set = set(features)
    freq = collections.defaultdict(int) #{feature:[num]}
    order =  {word: i for i, word in enumerate(features)}
    for r in responses:
        for f in set(r.split(' ')): # bc if repeated word, it will be counted twice
            if f in feature_set:
                freq[f] += 1  # {feature:num} for the sort purpose
                
    features.sort(key= lambda x: (-freq[x], order[x])) # - freq[x] for descending order
    return features



if __name__ == "__main__":
    print(sort_features(["easy", "touch"], ["i love the touch pad touch", "touch it was not easy to use"]))