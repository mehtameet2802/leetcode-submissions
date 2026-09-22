class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:

        def possible(val):
            trips = 0
            for t in time:
                trips += val // t
            
            return trips >= totalTrips
        
        left = min(time)
        right = totalTrips*left

        while left < right:
            mid = left + (right - left)//2

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        return left