class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        
        n = len(arr)
        
        dp = {}
        
        def solve(start):
            if start == n:
                return 0
            
            if start in dp:
                return dp[start]
            
            best = 0
            cur_max = 0
            
            for end in range(start,min(n,start+k)):
                cur_max = max(arr[end], cur_max)
                
                par_len = end - start + 1
                
                par_val = par_len * cur_max
                
                best = max(best, par_val + solve(end + 1))
            
            dp[start] = best
            
            return best
        
        return solve(0)

# TC - O(k^n)
# SC - O(n) recursion stack
        
