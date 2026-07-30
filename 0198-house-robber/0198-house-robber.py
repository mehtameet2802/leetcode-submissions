class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Pattern - Recursion

        TC - O(n)
        SC - O(n)
        '''

        mem = {}

        def helper(i):
            if i in mem:
                return mem[i]

            if i>=len(nums):
                return 0
            
            ans = max(helper(i+2)+nums[i],helper(i+1))
            mem[i] = ans
            return ans
        
        return helper(0)