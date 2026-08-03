class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        # '''
        # Pattern - Pre + Suf Sum

        # TC - O(N)
        # SC - O(N)
        # '''

        # pre_sum = [0]*len(nums)
        # suf_sum = [0]*len(nums)

        # n = len(nums)
        # for i in range(1,n):
        #     pre_sum[i] = nums[i-1] + pre_sum[i-1]
        
        # for i in range(n-2,-1,-1):
        #     suf_sum[i] = suf_sum[i+1] + nums[i+1]
        
        # for i in range(n):
        #     if pre_sum[i] == suf_sum[i]:
        #         return i
        
        # return -1


        '''
        Pattern - Pre + Suf Sum

        TC - O(N)
        SC - O(1)
        '''

        n = len(nums)
        pre_sum = 0
        total = sum(nums)
        
        for i in range(n):
            suf_sum = total - pre_sum - nums[i]
            if pre_sum == suf_sum:
                return i
            
            pre_sum = pre_sum + nums[i]
        
        return -1

