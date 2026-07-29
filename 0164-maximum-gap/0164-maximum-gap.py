class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums)<2:
            return 0
        
        nums = sorted(nums)

        diff = nums[1]-nums[0]
        ans = 0

        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            ans = max(ans,diff)
        
        return ans