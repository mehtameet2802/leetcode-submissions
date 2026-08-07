import math
from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        n = len(potions)

        for spell in spells:
            target = math.ceil(success/spell)

            start = bisect_left(potions, target)
            print(start)

            if start == -1 or start == n:
                ans.append(0)
            else:
                ans.append(n-start)
        
        return ans
