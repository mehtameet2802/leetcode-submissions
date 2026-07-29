from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        f_map = Counter(s)

        for ch in t:
            if ch not in f_map:
                return False
            
            f_map[ch]-=1
            if f_map[ch]<=0:
                f_map.pop(ch)
        
        if not f_map:
            return True
        
        return False