from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        elif len(s) == len(t):
            
            for ch in range(len(s)):
                countS = Counter(s)
                countT = Counter(t)
                
                return countS == countT