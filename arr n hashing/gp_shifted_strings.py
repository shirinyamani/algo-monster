import collections

def groupShiftedStrings(strs):
    shifted = collections.defaultdict(list) #{key: [values]}
    for s in strs:
        key = "" 
        for ch in range(1, len(s)): 
            key += str(ord(s[ch]) - ord(s[ch - 1])) # ord() returns the ascii value of a character
            print(key)

        shifted[key].append(s)

    return shifted.values()


if __name__ == "__main__":
    print(groupShiftedStrings(["acd", "dfg", "wyz", "yab", "mop",
                 "bdfh", "a", "x", "moqs"]))