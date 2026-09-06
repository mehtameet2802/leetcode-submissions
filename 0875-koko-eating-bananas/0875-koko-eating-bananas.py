from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        binary search on the speed range k, need min speed
        l = 1
        r = max(piles)

        possible func - 
        takes speed of input and checks if all banas can be eaten in h hours

        if possible - do r = mid
        else l = mid + 1

        '''

        def possible(speed):
            hours_taken = 0
            for pile in piles:
                hours_taken += ceil(pile/speed)
            
            return hours_taken <= h
        
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left