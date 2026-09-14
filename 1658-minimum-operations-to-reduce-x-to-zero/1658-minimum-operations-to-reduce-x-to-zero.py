class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
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
                length = max(length,right-left+1)

        if length == -1:
            return -1
        
        return len(nums) - length