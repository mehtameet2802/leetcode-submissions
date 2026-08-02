class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        idx_map = {}

        pre_sum = [0]*len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        sum = 0
        for i in range(len(nums)):
            pre_sum[i] = sum+nums[i]
            sum = pre_sum[i]
        
        ans = 0
        idx_map[0] = -1
        for i,num in enumerate(pre_sum):
            if num in idx_map:
                ans = max(ans,i-idx_map[num])
            else:
                idx_map[num] = i  
        
        return ans