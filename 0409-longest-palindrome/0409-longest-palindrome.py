from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        f_map = Counter(s)

        ans = 0
        odd = False
        for ch, f in f_map.items():
            ans += (f//2)*2

            if f%2:
                odd = True
        
        if odd:
            return ans+1
        return ans
        
        