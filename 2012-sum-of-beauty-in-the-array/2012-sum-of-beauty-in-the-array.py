class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:

        '''
        Pattern - Prefix Max + Suffix Min

        TC - O(N)
        SC - O(N)
        '''
        
        n = len(nums)
        pre = [0]*n
        pre_max = -float('inf')
        suf_min = float('inf')
        ans = 0

        for i in range(n-1):
            pre[i] = pre_max
            pre_max = max(pre_max,nums[i])
        pre[n-1] = pre_max
        
        for i in range(n-2,0,-1):
            suf_min = min(nums[i+1], suf_min)
            if nums[i] > pre[i] and nums[i] < suf_min:
                ans += 2
            elif nums[i] > nums[i-1] and nums[i] < nums[i+1]:
                ans += 1

        return ans

