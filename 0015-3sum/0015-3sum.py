class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        ans = set()
        
        for i in range(len(nums)):
            cur = nums[i] 
            seen = set()
            for j in range(i+1,len(nums)):
                target = 0 - cur - nums[j]
                if target in seen:
                    ans.add((cur,nums[j],target))
                seen.add(nums[j])
        
        return list(ans)
                