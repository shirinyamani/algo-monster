import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = collections.defaultdict(list) 
        for str in strs: 
            sorted_str = ''.join(sorted(str)) 
            anagrams[sorted_str].append(str)
        return anagrams.values()

                