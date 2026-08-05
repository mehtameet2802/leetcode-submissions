class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        '''
        Pattern - Sliding Window
        
        TC - O(N)
        SC - O(1)
        '''

        if k<=1:
            return 0
        
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