class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def helper(i, cur):
            if (i,cur) in dp:
                return dp[(i,cur)]

            if i == len(nums):
                return 1 if cur == target else 0
            
            dp[(i,cur)] = helper(i+1,cur-nums[i]) + helper(i+1, cur+nums[i])
            return dp[(i,cur)]

        return helper(0,0)