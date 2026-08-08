import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def cal(ele):
            ans = 0
            for num in nums:
                ans += math.ceil(num / ele)

            return ans

        l = 1
        r = max(nums)+1

        while l < r:
            mid = l + (r-l)//2
            if cal(mid) > threshold:
                l = mid + 1
            else:
                r = mid

        return l



