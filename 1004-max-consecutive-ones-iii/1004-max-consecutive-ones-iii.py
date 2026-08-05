class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        '''
        Pattern - Sliding Window

        TC - O(N)
        SC - 0(1)
        '''
        
        left = 0
        ans = 0
        cnt = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                cnt += 1
            

            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1

                left += 1
            
            ans = max(ans, right - left + 1)
    
        return ans