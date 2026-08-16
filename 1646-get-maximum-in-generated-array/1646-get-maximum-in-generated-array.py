class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n

        nums = [0]*(n+1)
        nums[1] = 1

        ans = 1

        for i in range(2,n+1):
            val = i//2
            if i%2 == 0:
                ans = max(ans, nums[val])
                nums[i] = nums[val]
            else:
                ans = max(ans, nums[val] + nums[val+1])
                nums[i] = nums[val] + nums[val+1]
        
        return ans

