class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        '''
        Pattern - Kadane Algorithm

        TC - O(N)
        SC - O(1)
        '''
        
        cur_max = cur_min = nums[0]
        ans = abs(nums[0])

        for num in nums[1:]:
            cur_max, cur_min = max(num, num+cur_max), min(num, num+cur_min)
            ans = max(ans, abs(num), abs(cur_max), abs(cur_min))
        
        return ans