class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        
        cur_max = cur_min = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            ans = max(ans, abs(num), abs(cur_max), abs(cur_min))
            cur_max, cur_min = max(num, num+cur_max), min(num, num+cur_min)
        
        return max(ans,abs(cur_max),abs(cur_min))