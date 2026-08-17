class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        def check(arr):
            arr1 = set(arr)

            if len(arr) != 2 and len(arr)!=3:
                return False

            if len(arr1) == 1:
                return True
            
            if len(arr1) == 3:
                for i in range(2):
                    if arr[i+1] - arr[i] != 1:
                        return False
                return True
        
            return False
        
        dp = {}

        def helper(i):
            if i in dp:
                return dp[i]

            if i>=len(nums):
                return True
            
            for j in range(i+2,min(i+4,len(nums)+1)):
                if check(nums[i:j]):
                    if helper(j):
                        dp[i] = True
                        return True
            
            dp[i] = False
            return False
        
        return helper(0)
