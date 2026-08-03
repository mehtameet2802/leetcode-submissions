class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_sum = [0]*len(nums)
        suf_sum = [0]*len(nums)

        n = len(nums)
        for i in range(1,n):
            pre_sum[i] = nums[i-1] + pre_sum[i-1]
        
        for i in range(n-2,-1,-1):
            suf_sum[i] = suf_sum[i+1] + nums[i+1]
        
        print(pre_sum)
        print(suf_sum)
        for i in range(n):
            if pre_sum[i] == suf_sum[i]:
                return i
        
        return -1
