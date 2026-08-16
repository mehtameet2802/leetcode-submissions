class Solution:
    def rob(self, nums: List[int]) -> int:
        # '''
        # Pattern - Recursion + DP

        # TC - O(n)
        # SC - O(n)
        # '''

        # mem = {}

        # def helper(i):
        #     if i in mem:
        #         return mem[i]

        #     if i>=len(nums):
        #         return 0
            
        #     ans = max(helper(i+2)+nums[i],helper(i+1))
        #     mem[i] = ans
        #     return ans
        
        # return helper(0)


        # '''
        # Pattern - DP

        # TC - O(n)
        # SC - O(1)
        # '''

        # n = len(nums)
        # if n<3:
        #     return max(nums)
        
        # last = nums[n-1]
        # prev1 = max(nums[n-1],nums[n-2])

        # for i in range(n-3,-1,-1):
        #     cur = max(nums[i]+last,prev1)
        #     last, prev1 = prev1, cur
        
        # return prev1










        if len(nums) < 2:
            return max(nums)

        n = len(nums)
        dp = [0]*len(nums)
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-2],nums[n-1])

        for i in range(n-3,-1,-1):
            dp[i] = max(dp[i+1],dp[i+2]+nums[i])
        
        return max(dp[0], dp[1])























