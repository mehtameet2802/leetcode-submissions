class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        ans = float('inf')
        cur = 0

        for right in range(len(nums)):
            
            cur += nums[right]

            while cur >= target:
                ans = min(ans, right - left + 1)

                cur -= nums[left]
                left += 1
            
                
        
        if ans == float('inf'):
            return 0
        return ans
