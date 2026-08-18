class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # dp = {}

        # def helper(i, cur):
        #     if (i,cur) in dp:
        #         return dp[(i,cur)]

        #     if i == len(nums):
        #         return 1 if cur == target else 0
            
        #     dp[(i,cur)] = helper(i+1,cur-nums[i]) + helper(i+1, cur+nums[i])
        #     return dp[(i,cur)]

        # return helper(0,0)


        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total + target) % 2:
            return 0

        subset_target = (total + target) // 2

        dp = [0] * (subset_target + 1)
        dp[0] = 1

        for num in nums:
            for cur in range(subset_target, num - 1, -1):
                dp[cur] += dp[cur - num]

        return dp[subset_target]