class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def calc(val):
            day = 1
            cur = 0
            for weight in weights:
                if cur + weight <= val:
                    cur += weight
                else:
                    cur = weight
                    day += 1

            return day

        while l < r:
            mid = l + (r-l)//2

            if calc(mid) > days:
                l = mid + 1
            else:
                r = mid
        
        return l

