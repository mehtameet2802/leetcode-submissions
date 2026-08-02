from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        f_map = Counter(s)

        ch_cnt = len(f_map.values())

        ans = 0
        for ch, f in f_map.items():
            if f%2 == 0:
                ans += f
                ch_cnt -= 1
            else:
                ans += (f//2)*2
                f_map[ch] = 1
        
        if ch_cnt:
            return ans+1
        return ans
        
        