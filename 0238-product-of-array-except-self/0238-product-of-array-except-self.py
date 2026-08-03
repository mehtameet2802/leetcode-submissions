class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [1]*n
        suf_prod = [1]*n

        for i in range(1,n):
            pre_prod[i] = pre_prod[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            suf_prod[i] = suf_prod[i+1]*nums[i+1]
        
        for i in range(n):
            pre_prod[i] *= suf_prod[i]
        
        return pre_prod