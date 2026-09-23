class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = [False]*(target + 1)
        dp[0] = True

        for num in nums:
            for cur in range(target,0,-1):
                if cur - num >= 0:
                    dp[cur] = dp[cur] or dp[cur-num]
        
        return dp[target]