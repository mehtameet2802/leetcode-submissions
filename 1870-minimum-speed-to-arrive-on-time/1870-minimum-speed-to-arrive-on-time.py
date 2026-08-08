import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        '''
        Pattern - Binary Search on Answer

        TC - O(N * log(10^7))
        SC - O(1)
        '''

        if len(dist) - 1 >= hour:
            return -1

        def timeTaken(speed):
            time = 0
            for i in range(len(dist)):
                if i == len(dist) - 1:
                    time += dist[i]/speed
                else:
                    time += math.ceil(dist[i]/speed)

            return time

        l = 1
        r = pow(10,7)

        while l < r:
            mid = l + (r-l)//2

            if timeTaken(mid) > hour:
                l = mid + 1
            else:
                r = mid
        
        return l
