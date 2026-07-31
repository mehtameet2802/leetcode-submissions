from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f_map = Counter(magazine)

        '''
        Pattern - Frequency Counter

        TC - O(n)
        SC - O(unique ch in magazine)
        '''

        for ch in ransomNote:
            if ch in f_map and f_map[ch]>0:
                f_map[ch] -= 1
                continue
            
            return False
        
        return True