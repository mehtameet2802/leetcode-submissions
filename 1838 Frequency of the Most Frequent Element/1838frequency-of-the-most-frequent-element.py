class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        s1 = nums[0]
        ans = 1
        i = 0 
        for j in range(1,len(nums)):
            s1+=nums[j]
            while s1+k<nums[j]*(j-i+1):
                s1-=nums[i]
                i+=1
            ans = max(ans,j-i+1)
        return ans

