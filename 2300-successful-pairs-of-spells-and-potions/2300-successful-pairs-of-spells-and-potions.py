import math
from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        Pattern - lower bound
        TC - O(M log M + N log M)
        SC - O(1)
        '''

        potions.sort()
        ans = []
        n = len(potions)

        for spell in spells:
            target = math.ceil(success/spell)

            start = bisect_left(potions, target)
            print(start)

            ans.append(n-start)
        
        return ans
