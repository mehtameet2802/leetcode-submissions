from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:

        '''
        Pattern - Greedy + HashMap

        TC - O(N)
        SC - O(U) - Unique freq

        '''

        f_map = Counter(s)

        # freq = sorted(f_map.values())

        seen = set()
        ans = 0

        for i in f_map.values():
            while i>0 and i in seen:
                i -= 1
                ans += 1
            seen.add(i)
        
        return ans