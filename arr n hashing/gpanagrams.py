import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = collections.defaultdict(list) #{key: [value]}
        
        for s in strs:
            res = ''.join(sorted(s)) # sort the string for each word for searching the char
            if res in anagram:
                anagram[res].append(s) # if the sorted string is already in the dictionary, append the word to the list
                
            else:
                anagram[res] = [s] # if the sorted string is not in the dictionary, create a new key and value pair
                
        return anagram.values()
                