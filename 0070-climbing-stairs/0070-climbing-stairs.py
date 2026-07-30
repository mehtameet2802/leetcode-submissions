class Solution:
    def climbStairs(self, n: int) -> int:

        mem = {}
        
        def helper(i):
            if i in mem:
                return mem[i]
            
            if i == n:
                return 1
            
            if i>n:
                return 0
            
            ans = helper(i+1) + helper(i+2)
            mem[i] = ans
            return ans
        
        return helper(0)