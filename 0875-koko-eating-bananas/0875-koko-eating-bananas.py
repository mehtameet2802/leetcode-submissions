import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        PAttern - Binary Search on ANswer
        TC - TC - O(n * log(max(weights)))
        SC - O(1)
        '''

        l = 1
        r = max(piles)

        def calc(rate):
            ans = 0
            for pile in piles:
                ans += math.ceil(pile/rate)
            
            return ans
        
        while l < r:
            mid = l + (r-l)//2

            if calc(mid) > h:
                l = mid + 1
            else:
                r = mid
        
        return l