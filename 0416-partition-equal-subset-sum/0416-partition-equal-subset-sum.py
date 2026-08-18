class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 :
            return False

        target = total // 2
        dp = {}

        def helper(i,target):
            if target == 0:
                return True
            
            if target<0:
                return False
            
            if i>=len(nums):
                return False

            if (i,target) in dp:
                return dp[(i,target)]
            
            ans = helper(i+1, target - nums[i]) or helper(i+1, target)
            dp[(i,target)] = ans
            return ans
            
        
        return helper(0, target)
            