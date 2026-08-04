class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        else: 
            counts = {}
            for char in s:
                counts[char] = counts.get(char, 0) + 1
                from collections import Counter
                return Counter(s) == Counter(t)