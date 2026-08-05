class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Pattern - Sliding window

        TC - O(N)
        SC - O(1)
        '''
        
        left = 0
        ans = 0
        cnt = 0
        k = 1

        for right in range(len(nums)):
            if nums[right] == 0:
                cnt += 1

            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans - 1 