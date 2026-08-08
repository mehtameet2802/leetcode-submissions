class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        '''
        Pattern - BInary Search on Answer
        TC - O(N log(max(time)-min(time)))
        SC - O(1)
        '''

        def tripsCompleted(curTime):
            trips = 0
            for cur in time:
                if cur <= curTime:
                    trips += curTime // cur
            
            return trips

        l = min(time)
        r = min(time)*totalTrips

        while l < r:
            mid = l + (r-l)//2

            if tripsCompleted(mid) < totalTrips:
                l = mid + 1
            else:
                r = mid
        
        return l