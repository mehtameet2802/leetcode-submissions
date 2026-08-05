class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        left = 0
        ans = 0
        cur = 1

        for right in range(len(nums)):
            cur *= nums[right]

            while cur >= k and left < right:
                cur = cur / nums[left]
                left += 1
            
            if cur < k:
                ans += (right - left + 1)
        
        return ans