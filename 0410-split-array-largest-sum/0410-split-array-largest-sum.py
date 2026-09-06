class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        if k == 1:
            return right
        
        def possible(capacity):
            groups = 0
            cur_capacity = capacity

            for num in nums:
                if num > cur_capacity:
                    groups += 1
                    cur_capacity = capacity
                
                cur_capacity -= num

            groups += 1
            return groups <= k
        

        while left < right:
            mid = left + (right - left) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left