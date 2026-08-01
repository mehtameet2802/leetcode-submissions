class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_ele = nums[0]
        ans = -1

        for i in range(1,len(nums)):
            min_ele = min(min_ele, nums[i])

            if min_ele < nums[i]:
                ans = max(ans, nums[i]-min_ele)
        
        return ans