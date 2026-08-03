class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''
        Pattern - Pre + Suf
        TC - O(N)
        SC - O(N)
        '''

        n = len(nums)
        pre_prod = [1]*n

        for i in range(1,n):
            pre_prod[i] = pre_prod[i-1]*nums[i-1]

        suffix = 1
        for i in range(n-2,-1,-1):
            suffix = suffix*nums[i+1]
            pre_prod[i] *= suffix
        
        return pre_prod