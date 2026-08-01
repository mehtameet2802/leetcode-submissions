class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0]*n
        suf_sum = [0]*n

        pre_sum[0] = 0
        suf_sum[n-1] = 0

        for i in range(1,len(nums)):
            pre_sum[i] = nums[i-1] + pre_sum[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            suf_sum[i] = nums[i+1] + suf_sum[i+1]

        for i in range(len(nums)):
            if pre_sum[i] == suf_sum[i]:
                return i

        return -1