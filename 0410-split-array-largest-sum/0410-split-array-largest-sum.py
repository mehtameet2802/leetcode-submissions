class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possible(val):
            cur_val = val
            cnt = 1

            for num in nums:
                if cur_val >= num:
                    cur_val -= num
                else:
                    cnt += 1
                    cur_val = val - num
        
            return cnt <= k

        l = max(nums)
        r = sum(nums)

        while l<r:
            mid = l + (r-l)//2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l








      