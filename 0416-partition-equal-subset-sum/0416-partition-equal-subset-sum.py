class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # total = sum(nums)

        # if total % 2 :
        #     return False

        # target = total // 2
        # dp = {}

        # def helper(i,target):
        #     if target == 0:
        #         return True
            
        #     if target<0:
        #         return False
            
        #     if i>=len(nums):
        #         return False

        #     if (i,target) in dp:
        #         return dp[(i,target)]
            
        #     ans = helper(i+1, target - nums[i]) or helper(i+1, target)
        #     dp[(i,target)] = ans
        #     return ans
            
        
        # return helper(0, target)


        total = sum(nums)

        if total % 2 :
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:

            for t in range(target, num-1, -1):
                dp[t] = dp[t] or dp[t-num]
            
        return dp[target]
            
        
        