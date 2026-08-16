class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        day = {
            0:1,
            1:7,
            2:30
        }
        
        dp = {}

        def helper(i, reach):

            if (i,reach) in dp:
                return dp[(i,reach)]

            if i >= len(days):
                return 0
            
            ans = float('inf')

            if days[i]<=reach:
                ans = helper(i+1, reach)
                dp[(i,reach)] = ans
                return ans

            for j in range(len(costs)):
                ans = min(ans, costs[j] + helper(i+1,days[i] + day[j]-1))
            
            dp[(i,reach)] = ans
            return ans

        return helper(0, 0)

