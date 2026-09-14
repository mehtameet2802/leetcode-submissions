class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # ans = float('inf')

        # def helper(val,left,right,opt):
        #     nonlocal ans

        #     if val == 0:
        #         ans = min(ans,opt)
        #         return
            
        #     if val < 0 or left > right:
        #         return

        #     helper(val-nums[left], left+1, right, opt+1)
        #     helper(val-nums[right], left, right-1, opt+1)
        
        # helper(x,0,len(nums)-1,0)
        # return -1 if ans == float('inf') else ans

        total = sum(nums)

        target = total - x

        if target < 0:
            return -1
        
        if target == 0:
            return len(nums)

        left = 0
        length = -1
        window_sum = 0

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum > target:
                window_sum -= nums[left]
                left += 1
            
            if window_sum == target:
                length = max(length, right-left+1)
            
        
        if length == -1:
            return -1
        
        return len(nums) - length

