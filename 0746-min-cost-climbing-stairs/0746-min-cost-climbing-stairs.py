class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # '''
        # Pattern - Recursion + DP

        # TC - O(n)
        # SC - O(n)
        # '''

        # mem = {}

        # def helper(i):
        #     if i in mem:
        #         return mem[i]

        #     if i>=len(cost):
        #         return 0
            
        #     ans = min(helper(i+1), helper(i+2)) + cost[i]
        #     mem[i] = ans
        #     return ans
        
        # return min(helper(0), helper(1))


        '''
        Pattern - DP

        TC - O(n)
        SC - O(1)
        '''
        
        n = len(cost)
        prev1 = cost[n-1] 
        prev2 = min(cost[n-2],cost[n-2]+cost[n-1])

        for i in range(n-3,-1,-1):
            cur = min(prev1,prev2) + cost[i]
            prev1, prev2 = prev2, cur
        
        return min(prev1, prev2)