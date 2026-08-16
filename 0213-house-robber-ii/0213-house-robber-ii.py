class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # '''
        # Pattern - 

        # TC - O(n)
        # SC - O(n)
        # '''

        # mem = {}

        # n = len(nums)

        # if n == 1:
        #     return nums[0]
        
        # def helper(i, first_taken):
        #     if (i,first_taken) in mem:
        #         return mem[(i,first_taken)]

        #     if i>=n:
        #         return 0
            
        #     if i == n-1:
        #         if first_taken:
        #             return 0
        #         return nums[i]
            
        #     ans = max(helper(i+2,first_taken)+nums[i], helper(i+1,first_taken))
        #     mem[(i,first_taken)] = ans
        #     return ans
        
        # return max(helper(0,True), helper(1, False))


        # '''
        # Pattern - 

        # TC - O(n)
        # SC - O(1)
        # '''

        # n = len(nums)

        # if n == 1:
        #     return nums[0]
        
        # def robber(s,e):

        #     last = nums[e]
        #     prev1 = max(nums[e-1],last)

        #     for i in range(e-2,s-1,-1):
        #         cur = max(nums[i]+last,prev1)
        #         last, prev1 = prev1, cur
            
        #     return prev1
        
        # return max(robber(0,n-2), robber(1, n-1))










        if len(nums) == 1:
            return nums[0]

        def robber(start,end):

            last1 = nums[end]
            last2 = max(nums[end-1],nums[end])

            for i in range(end-2,start-1,-1):
                cur = max(last2, last1+nums[i])
                last2, last1 = cur, last2
            
            return last2
        
        return max(robber(0,len(nums)-2),robber(1,len(nums)-1))








