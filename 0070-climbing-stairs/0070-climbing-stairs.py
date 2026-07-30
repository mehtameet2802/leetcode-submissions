class Solution:
    def climbStairs(self, n: int) -> int:

        # '''
        # Pattern - Recursion + DP

        # TC - O(n)
        # SC - O(n)
        # '''

        # mem = {}
        
        # def helper(i):
        #     if i in mem:
        #         return mem[i]
            
        #     if i == n:
        #         return 1
            
        #     if i>n:
        #         return 0
            
        #     ans = helper(i+1) + helper(i+2)
        #     mem[i] = ans
        #     return ans
        
        # return helper(0)


        '''
        Pattern - Recursion + DP

        TC - O(n)
        SC - O(1)
        '''

        if n<=2:
            return n

        prev_1 = 1
        prev_2 = 2
        
        for _ in range(n-3,-1,-1):
            prev_3 = prev_1 + prev_2
            prev_1, prev_2 = prev_2, prev_3

        return prev_2