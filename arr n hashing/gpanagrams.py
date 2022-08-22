import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = collections.defaultdict(list) #{key: [value]}
        
        for s in strs:
            res = ''.join(sorted(s))
            if res in anagram:
                anagram[res].append(s)
                
            else:
                anagram[res] = [s]
                
        return anagram.values()
                